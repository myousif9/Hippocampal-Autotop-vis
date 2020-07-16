import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
import seaborn as sns 
from os.path import join

data = pd.read_pickle(snakemake.input[0])

y_fields = [key for key in data.keys() if key not in ['subject','labels','hemi','x_label','img']]
hemi_count = np.unique(data.hemi)

def violinplot_group(dataframe, feature, hemi='', log=False):
    """
    violin group plotting function based on hippocampal subfields
    feature --> feature to plot  
    hemi --> '','all','L' or 'R'
    """
    num_idx =~pd.isnull(dataframe[feature])
    if log == True:
        if hemi == '':
            sns.violinplot(x=dataframe['labels'][num_idx],y=np.log10(dataframe[feature][num_idx]))
        elif hemi == 'all':
            sns.violinplot(x=dataframe['labels'][num_idx],y=np.log10(dataframe[feature][num_idx]),hue=dataframe['hemi'][num_idx])
        else:
            sns.violinplot(x=dataframe['labels'][num_idx][dataframe[num_idx]['hemi'] == hemi],y=np.log10(dataframe[feature][num_idx][dataframe[num_idx]['hemi'] == hemi]))
    else:
        if hemi == '':
            sns.violinplot(x=dataframe['labels'][num_idx],y=dataframe[feature][num_idx])
        elif hemi == 'all':
            sns.violinplot(x=dataframe['labels'][num_idx],y=dataframe[feature][num_idx],hue=dataframe['hemi'][num_idx])
        else:
            sns.violinplot(x=dataframe['labels'][num_idx][dataframe[num_idx]['hemi'] == hemi],y=dataframe[feature][num_idx][dataframe[num_idx]['hemi'] == hemi])

#         sns.violinplot(x=dataframe['labels'][num_idx],y=dataframe[feature][num_idx],hue=dataframe['hemi'][num_idx])
    
    locs, labels = plt.xticks()
    plt.xticks(locs,['subiculumn','CA1','CA2','CA3','CA4'])
    
def lineplot_AP_group(dataframe, feature, hemi, subfield='all', grouping_feature=''):
    if subfield == 'all':
        if (grouping_feature==''):
            sns.lineplot(x=dataframe[dataframe.hemi==hemi]['x_label'], y=dataframe[dataframe.hemi==hemi][feature])
        else:
            sns.lineplot(x=dataframe[dataframe.hemi==hemi]['x_label'], y=dataframe[dataframe.hemi==hemi][feature], hue=dataframe[dataframe.hemi==hemi][grouping_feature])
    elif (subfield == 1) or (subfield.lower() == 'subiculumn') or subfield.lower() == 'sub':
        sub = 1
        if (grouping_feature==''):
            sns.lineplot(x=dataframe[dataframe.hemi==hemi][dataframe.labels == sub]['x_label'], y=dataframe[dataframe.hemi==hemi][dataframe.labels == sub][feature])
        else:
            sns.lineplot(x=dataframe[dataframe.hemi==hemi][dataframe.labels == sub]['x_label'], y=dataframe[dataframe.hemi==hemi][dataframe.labels == sub][feature], hue=dataframe[dataframe.hemi==hemi][dataframe.labels == sub][grouping_feature])
    elif (subfield == 2) or (subfield.lower() == 'ca1'):
        sub = 2
        if (grouping_feature==''):
            sns.lineplot(x=dataframe[dataframe.hemi==hemi][dataframe.labels == sub]['x_label'], y=dataframe[dataframe.hemi==hemi][dataframe.labels == sub][feature])
        else:
            sns.lineplot(x=dataframe[dataframe.hemi==hemi][dataframe.labels == sub]['x_label'], y=dataframe[dataframe.hemi==hemi][dataframe.labels == sub][feature], hue=dataframe[dataframe.hemi==hemi][dataframe.labels == sub][grouping_feature])
    elif (subfield == 3) or (subfield.lower() == 'ca2'):
        sub = 3
        if (grouping_feature==''):
            sns.lineplot(x=dataframe[dataframe.hemi==hemi][dataframe.labels == sub]['x_label'], y=dataframe[dataframe.hemi==hemi][dataframe.labels == sub][feature])
        else:
            sns.lineplot(x=dataframe[dataframe.hemi==hemi][dataframe.labels == sub]['x_label'], y=dataframe[dataframe.hemi==hemi][dataframe.labels == sub][feature], hue=dataframe[dataframe.hemi==hemi][dataframe.labels == sub][grouping_feature])
    elif (subfield == 4) or (subfield.lower() == 'ca3'):
        sub = 4
        if (grouping_feature==''):
            sns.lineplot(x=dataframe[dataframe.hemi==hemi][dataframe.labels == sub]['x_label'], y=dataframe[dataframe.hemi==hemi][dataframe.labels == sub][feature])
        else:
            sns.lineplot(x=dataframe[dataframe.hemi==hemi][dataframe.labels == sub]['x_label'], y=dataframe[dataframe.hemi==hemi][dataframe.labels == sub][feature], hue=dataframe[dataframe.hemi==hemi][dataframe.labels == sub][grouping_feature])
    elif (subfield == 5) or (subfield.lower() == 'ca4') or (subfield.lower() == 'dentate gyrus') or (subfield.lower() == 'dg'):
        sub = 5
        if (grouping_feature==''):
            sns.lineplot(x=dataframe[dataframe.hemi==hemi][dataframe.labels == sub]['x_label'], y=dataframe[dataframe.hemi==hemi][dataframe.labels == sub][feature])
        else:
            sns.lineplot(x=dataframe[dataframe.hemi==hemi][dataframe.labels == sub]['x_label'], y=dataframe[dataframe.hemi==hemi][dataframe.labels == sub][feature], hue=dataframe[dataframe.hemi==hemi][dataframe.labels == sub][grouping_feature])
    




# def boxplot_group_subfields(data, hemi_count, feature):
#     plt.figure(figsize=(10,6))
#     for k in range(1,6):
#         plt.subplot(1,5,k)
#         if hemi_count==2:
#             sns.boxplot(x='subject',y=feature,hue='hemi',data=data[data['labels'] == k])
#         else:
#             sns.boxplot(x='subject',y=feature,data=data[data['labels'] == k])
#         plt.title(' '.join([str(k),feature]))
#     plt.tight_layout()
#     plt.savefig(join('output','_'.join([feature,'boxplot_group.png'])))

# def lineplot_group_AP(data, feature):
#     subjects = np.unique(data.subject)
#     plt.figure(figsize=(20,7))
#     for k in range(1,6):
#         plt.subplot(1,5,k)
#         sns.lineplot(x='x_label',y=feature,hue='subject',data=data[data['labels'] == k])
#         plt.title(' '.join([str(k),feature]))
#     plt.tight_layout()
#     plt.savefig(join('output','_'.join([feature,'lineplot_group.png'])))

# hemi = snakemake.params['hemi']
for hemi in snakemake.wildcards['hemi']:
    for feature in y_fields:
        plt.figure()
        violinplot_group(data, feature)
        plt.savefig(join('output','_'.join([snakemake.wildcards['subject'],'hemi-'+hemi,feature,'violinplot_group.png'])))

        plt.figure()
        lineplot_AP_group(data, feature,hemi='L')
        plt.savefig(join('output','_'.join([snakemake.wildcards['subject'],'hemi-'+hemi,feature,'lineplot_group.png'])))
        # boxplot_group_subfields(data,feature)
        # lineplot_group_AP(data,feature)

# data.to_csv(snakemake.output[0],index=False)