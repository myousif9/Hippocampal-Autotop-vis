from scipy.io import loadmat
import matplotlib.pyplot as plt
import pandas as pd
from skimage.transform import rescale

unfold = loadmat(snakemake.input.unfold_mat)
surf= loadmat(snakemake.input.surf_mat)
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