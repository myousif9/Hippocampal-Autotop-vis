from scipy.io import loadmat
from scipy.interpolate import griddata
import pandas as pd 
import numpy as np 
from skimage.transform import rescale 
from sklearn.preprocessing import scale 
import os

unfold = loadmat(snakemake.input.unfold_mat)
surf = loadmat(snakemake.input.surf_mat)
boundary = loadmat(snakemake.input.boundary_mat)


def gen_data_table(img_mat,img_idx,boundary_mat,subject,output): 
    # img_mat = loadmat(input_mat)
    # boundary_mat= loadmat(boundary_mat)
    
    subfield_map = np.round(rescale(boundary_mat['subfield_avg'],scale=0.5,preserve_range=True))

    x = np.arange(0,256)
    x = np.reshape(x,(-1,1))
    x_mat = np.repeat(x,128,axis=1)

    df = pd.DataFrame({'subject':[subject for x in range(len(subfield_map.flatten()))],
                       'labels': subfield_map.flatten().astype(int),
                       'x_label': x_mat.flatten(),
                       str(img_idx): img_mat[img_idx].flatten()})
    df.to_pickle(output,index=False,header=False)
    

def gen_fig(img_mat,img_idx,boundary_mat,output_npz,output_img):
    from scipy.interpolate import griddata
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
    
    img_interp = griddata((x1,y1), newimg.ravel(), (xx,yy), method='cubic')
    
    # saving interpolated image and 
    npz_dict = {img_idx+'_img_nointer':img_nointerp.transpose(), img_idx+'_img_interp':img_interp.transpose()}
    if os.path.exists(output_img):
        npz_load = np.load(output_npz)
        npz_load.update(npz_dict)
        np.savez(output_npz, npz)
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


gen_data_table(snakemake.input.surf_mat, 'streamlengths', snakemake.input.boundary_mat, snakemake.input.sub, snakemake.output.table)
gen_data_table(snakemake.input.surf_mat, 'GI', snakemake.input.boundary_mat, snakemake.input.sub, snakemake.output.data_table)
gen_data_table(snakemake.input.surf_mat, 'qMap', snakemake.input.boundary_mat, snakemake.input.sub, snakemake.output.data_table)

gen_fig(snakemake.input.surf_mat, 'streamlengths', snakemake.input.boundary_mat, snakemake.input.sub, snakemake.output.unfold_npz, snakemake.output.unfold_img)
gen_fig(snakemake.input.surf_mat, 'GI', snakemake.input.boundary_mat, snakemake.input.sub,  snakemake.output.unfold_npz, snakemake.output.data_table)
gen_fig(snakemake.input.surf_mat, 'qMap', snakemake.input.boundary_mat, snakemake.input.sub,  snakemake.output.unfold_npz, snakemake.output.data_table)