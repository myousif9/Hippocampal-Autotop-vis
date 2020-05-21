from scipy.io import loadmat
from scipy import interpolate
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from skimage.transform import rescale
from sklearn.preprocessing import scale

unfold = loadmat(snakemake.input.unfold_mat[0])
surf= loadmat(snakemake.input.surf_mat[0])
boundary = loadmat(snakemake.input.boundary_mat)

thickness = surf['streamlengths']

thickness_df = pd.DataFrame(thickness)
thickness_df.interpolate('linear',inplace=True)

f = plt.figure()
ax = f.add_subplot(111)
ax.yaxis.tick_right()
plt.imshow(surf['qMap'].transpose(),origin='lower')
plt.contour(rescale(boundary['subfields_avg'].transpose(), scale =0.5),colors =['white'])
plt.yticks([0,40,70,100,120],labels=['Sub','CA1','CA2','CA3','CA4'])
plt.tick_params(length=0)
plt.xticks([])
f.savefig(snakemake.output[0])

def gen_fig(mat_path,img_idx,boundary_path,output):
    img = loadmat(mat_path)
    img = img[img_idx]
    
    boundary = loadmat(boundary_path)
    boundary = boundary['subfields_avg']
    
    # interpolating step for missing points
    x = np.arange(0, img.shape[1])
    y = np.arange(0, img.shape[0])
    
    img = np.ma.masked_invalid(img)
    xx, yy =np.meshgrid(x,y)
    
    x1 = xx[~img.mask]
    y1 = yy[~img.mask]
    newimg = img[~img.mask]
    
    img_interp = interpolate.griddata((x1,y1), newimg.ravel(), (xx,yy), method='cubic')
    
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
    f.savefig(output)