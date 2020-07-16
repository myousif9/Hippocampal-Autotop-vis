from scipy.io import loadmat
from scipy import interpolate
import pandas as pd 
import numpy as np 
from skimage.transform import rescale 
from sklearn.preprocessing import scale 
import os
import matplotlib.pyplot as plt


# unfold = loadmat(snakemake.input[0])
# surf = loadmat(snakemake.input[1])
boundary = loadmat(snakemake.input[0])
subject = snakemake.input[1].split('/')[-3]


def gen_data_table(img_mat,img_idx,img_type,hemi,boundary_mat,subject,output_npz,output): 
    # img_mat = loadmat(input_mat)
    # boundary_mat= loadmat(boundary_mat)
    img_modality = img_type
    subfield_map = np.round(rescale(boundary_mat['subfields_avg'],scale=0.5,preserve_range=True))

    x_coor = np.arange(0,256)
    x_coor = np.reshape(x_coor,(-1,1))
    x_mat = np.repeat(x_coor,128,axis=1)

    img = img_mat[img_idx]
    img_mean, img_std = np.mean(img), np.std(img)
    lower_bound, upper_bound = img_mean-(3*img_std), img_mean+(3*img_std)
    img[np.logical_or(img<lower_bound,img>upper_bound)] = np.nan

    if os.path.isfile(output) == False:
        df = pd.DataFrame({'subject':[subject for x in range(len(subfield_map.flatten()))],
                        'hemi':[hemi for x in range(len(subfield_map.flatten()))],
                        'labels': subfield_map.flatten().astype(int),
                        'x_label': x_mat.flatten(),
                        'img':[img_type for x in range(len(subfield_map.flatten()))],
                        str(img_idx): img.flatten()})
        # df['subject'] = df.subject.astype('category')
        # df['hemi'] = df.labels.astype('category')
        df.to_pickle(output)
    else:
        df_pickle = pd.read_pickle(output)
        df_pickle[str(img_idx)] = img_mat[img_idx].flatten()
        df_pickle.to_pickle(output)

    img_nointerp =  img
    
    # interpolating step for missing points
    x = np.arange(0, img.shape[1])
    y = np.arange(0, img.shape[0])
    
    img = np.ma.masked_invalid(img)
    xx, yy =np.meshgrid(x,y)
    
    x1 = xx[~img.mask]
    y1 = yy[~img.mask]
    newimg = img[~img.mask]
    
    img_interp = interpolate.griddata((x1,y1), newimg.ravel(), (xx,yy), method='nearest')
    
    # saving interpolated image and 
    if img_nointerp == (128, 256):
        npz_dict = {img_idx+'_hemi-'+hemi+'_img_nointer':img_nointerp, img_idx+'_img_interp':img_interp}
    else:
        npz_dict = {img_idx+'_hemi-'+hemi+'_img_nointer':img_nointerp.transpose(), img_idx+'_img_interp':img_interp.transpose()}
    if os.path.isfile(output_npz):
        npz_load = dict(np.load(output_npz,allow_pickle=True))
        npz_load.update(npz_dict)
        np.savez(output_npz, **npz_load)
    else:
        np.savez(output_npz, **npz_dict,allow_pickle=True)


def find_output_path(key, out_paths):
    for path in out_paths:
        if key in path:
            return path
print(snakemake.params['hemi'])
for mat_path in snakemake.input[1::]:
    mat = loadmat(mat_path)
    img_mod = mat_path.split('/')[-2]
    for count, key in enumerate(mat.keys()):
        for hemi in snakemake.params['hemi']:
            if np.shape(mat[key]) == (256, 128):
                gen_data_table(mat, key,img_mod, hemi, boundary,subject,snakemake.output[0],snakemake.output[1])
            # gen_fig(mat, key, hemi, boundary, snakemake.output[0], find_output_path(key,snakemake.output[2::]))

# gen_data_table(surf, 'streamlengths', boundary, subject, snakemake.output[1])
# gen_data_table(surf, 'GI', boundary, subject, snakemake.output[1])
# gen_data_table(surf, 'qMap', boundary, subject, snakemake.output[1])


# gen_fig(surf, 'streamlengths', boundary, snakemake.output[0], snakemake.output[2])
# gen_fig(surf, 'GI', boundary,  snakemake.output[0], snakemake.output[3])
# gen_fig(surf, 'qMap', boundary,  snakemake.output[0], snakemake.output[4])