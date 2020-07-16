import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
import seaborn as sns 
from os.path import join

data = pd.read_pickle(snakemake.input[0])

y_fields = [key for key in data.keys() if key not in ['subject','hemi','labels','x_label']]
hemi_count = len(np.unique(data.hemi))

def boxplot_subfields(data, hemi_count, feature, subject):
    plt.figure()
    if hemi_count == 2:
        sns.boxplot(x='labels',y=feature, hue='hemi',  data =data)
    else:
        sns.boxplot(x='labels',y=feature, data =data)
    plt.title(' '.join([subject,feature]))
    plt.savefig(join('output','_'.join([subject,feature,'boxplot.png'])))
    
# def boxplot_group_subfields(data,feature):
#     plt.figure(figsize=(10,6))
#     for k in range(1,6):
#         plt.subplot(1,5,k)
#         sns.boxplot(x='subject',y=feature,data=data[data['labels'] == k])
#         plt.title(' '.join([str(k),feature]))
#     plt.tight_layout()
#     plt.savefig(join('output','_'.join([feature,'group.png'])))
        
def lineplot_AP(data, feature, subject):
    # print(data.columns.values)
    # print(data['x_label'].dtype)
    # print(data[feature].dtype)
    # print(data['labels'].dtype)
    # print(data.feature)
    # print(str(feature))
    plt.figure()
    sns.lineplot(x='x_label',y=str(feature).strip(),hue='labels',data=data)
    plt.savefig(join('output','_'.join([subject,feature,'lineplot.png'])))
    
# def lineplot_group_AP(data,feature):
#     subjects = np.unique(data.subject)
#     plt.figure(figsize=(20,7))
#     for k in range(1,6):
#         plt.subplot(1,5,k)
#         sns.lineplot(x='subject',y=feature,hue='labels', data=data[data['labels'] == k])
#         plt.title(' '.join([str(k),feature]))
#     plt.tight_layout()
#     plt.savefig(join('output','_'.join([feature,'group.png'])))
    
    
for feature in y_fields:
    # print(feature)
    for sub in np.unique(data.subject):
        boxplot_subfields(data,hemi_count,feature,sub)
        lineplot_AP(data,feature,sub)

    # boxplot_group_subfields(data,feature)
    # lineplot_group_AP(data,feature)

# data.to_csv(snakemake.output[0],index=False)