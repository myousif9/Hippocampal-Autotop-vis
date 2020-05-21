from scipy.io import loadmat
from scipy import interpolate
import pandas as pd 
import numpy as np 
from skimage.transform import rescale 
from sklearn.preprocessing import scale 
import os
import matplotlib.pyplot as plt

unfold = loadmat(snakemake.input[0])
surf = loadmat(snakemake.input[1])
boundary = loadmat(snakemake.input[2])
subject = snakemake.input[0].split('_')[0]

def gen_data_table(img_mat,img_idx,boundary_mat,subject,output): 
    # img_mat = loadmat(input_mat)
    # boundary_mat= loadmat(boundary_mat)
    
    subfield_map = np.round(rescale(boundary_mat['subfields_avg'],scale=0.5,preserve_range=True))

    x = np.arange(0,256)
    x = np.reshape(x,(-1,1))
    x_mat = np.repeat(x,128,axis=1)

    df = pd.DataFrame({'subject':[subject for x in range(len(subfield_map.flatten()))],
                       'labels': subfield_map.flatten().astype(int),
                       'x_label': x_mat.flatten(),
                       str(img_idx): img_mat[img_idx].flatten()})
    df.to_pickle(output)
    

def gen_fig(img_mat,img_idx,boundary_mat,output_npz,output_img):
    # img = loadmat(mat_path)
    # img = img[img_idx]
    
    img = img_mat[img_idx]
    img_nointerp =  img

    # boundary = loadmat(boundary_path)
    boundary = boundary_mat['subfields_avg']
    
    # interpolating step for missing points
    x = np.arange(0, img.shape[1])
    y = np.arange(0, img.shape[0])
    
    img = np.ma.masked_invalid(img)
    xx, yy =np.meshgrid(x,y)
    
    x1 = xx[~img.mask]
    y1 = yy[~img.mask]
    newimg = img[~img.mask]
    
    img_interp = interpolate.griddata((x1,y1), newimg.ravel(), (xx,yy), method='cubic')
    
    # saving interpolated image and 
    npz_dict = {img_idx+'_img_nointer':img_nointerp.transpose(), img_idx+'_img_interp':img_interp.transpose()}
    if os.path.isfile(output_npz):
        npz_load = dict(np.load(output_npz,allow_pickle=True))
        new_npz = [npz_load,npz_dict]
        np.savez(output_npz, new_npz)
    else:
        np.savez(output_npz, npz_dict)

    #plotting figure
    f = plt.figure()
    ax = f.add_subplot(111)
    ax.yaxis.tick_right()
    plt.imshow(img_interp.transpose(),origin='lower')
    plt.colorbar(orientation='horizontal',pad=0.1)
    plt.contour(rescale(boundary.transpose(), scale =0.5),colors =['white'])
    plt.yticks([0,40,70,100,120],labels=['Sub','CA1','CA2','CA3','CA4'])
    plt.tick_params(length=0)
    plt.xticks([])
    f.savefig(output_img)


gen_data_table(surf, 'streamlengths', boundary, subject, snakemake.output[2])
gen_data_table(surf, 'GI', boundary, subject, snakemake.output[2])
gen_data_table(surf, 'qMap', boundary, subject, snakemake.output[2])

gen_fig(surf, 'streamlengths', boundary, snakemake.output[1], snakemake.output[0])
gen_fig(surf, 'GI', boundary,  snakemake.output[1], snakemake.output[0])
gen_fig(surf, 'qMap', boundary,  snakemake.output[1], snakemake.output[0])