from scipy.io import loadmat
from scipy import interpolate
from scipy.ndimage import gaussian_filter
import pandas as pd 
import numpy as np 
from skimage.transform import rescale 
from sklearn.preprocessing import scale 
import os
import matplotlib.pyplot as plt

import matplotlib
matplotlib.use('Agg')

# unfold = loadmat(snakemake.input[0])
# surf = loadmat(snakemake.input[1])
boundary = loadmat(snakemake.input[0])
subject = snakemake.input[1].split('/')[-3]

def gen_fig(img_mat,img_idx,hemi,boundary_mat,output_img):
    # img = loadmat(mat_path)
    # img = img[img_idx]
    
    img = img_mat[img_idx]

    img_mean, img_std = np.mean(img), np.std(img)
    lower_bound, upper_bound = img_mean - img_std*3, img_mean + img_std*3

    img[np.logical_or(img>upper_bound,img<lower_bound)] = np.nan 

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
    
    img_interp = interpolate.griddata((x1,y1), newimg.ravel(), (xx,yy), method='nearest')
    
    img_interp = gaussian_filter(img_interp,sigma=1)
    # saving interpolated image and 
    # if img_nointerp == (128, 256):
    #     npz_dict = {img_idx+'_hemi-'+hemi+'_img_nointer':img_nointerp, img_idx+'_img_interp':img_interp}
    # else:
    #     npz_dict = {img_idx+'_hemi-'+hemi+'_img_nointer':img_nointerp.transpose(), img_idx+'_img_interp':img_interp.transpose()}
    # if os.path.isfile(output_npz):
    #     npz_load = dict(np.load(output_npz,allow_pickle=True))
    #     npz_load.update(npz_dict)
    #     np.savez(output_npz, **npz_load)
    # else:
    #     np.savez(output_npz, **npz_dict,allow_pickle=True)

    #plotting figure
    f = plt.figure()
    ax = f.add_subplot(111)
    ax.yaxis.tick_right()
    plt.imshow(img_interp.transpose(),cmap=snakemake.params['cmap'],origin='lower')
    # f.set_cmap(snakemake.parms[0])
    plt.colorbar(orientation='horizontal',pad=0.1)
    plt.contour(rescale(boundary.transpose(), scale =0.5),colors =['white'])
    plt.yticks([0,40,70,100,120],labels=['Sub','CA1','CA2','CA3','CA4'])
    plt.tick_params(length=0)
    plt.xticks([])
    f.savefig(output_img)



def find_output_path(key, out_paths):
    for path in out_paths:
        if key in path:
            return path


# mat = loadmat(mat_path)
# hemi = snakemake.wildcards['hemi']
    # img_mod = mat_path.split('/')[-2]
    # for count, key in enumerate(mat.keys()):
    #     if np.shape(mat[key]) == (256, 128):
            # gen_data_table(mat, key,img_mod, hemi, boundary,subject,snakemake.output[1])
gen_fig(loadmat(snakemake.input[1]), snakemake.wildcards['feature'], snakemake.wildcards['hemi'], boundary, snakemake.output[0])
