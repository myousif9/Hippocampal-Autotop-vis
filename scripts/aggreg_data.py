import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import os



# def visualize_subj(pickle):
#     subjects = np.unique(pickle.subject)

#     for sub in subjects:
#         sub_df = pickle[pickle.subject == sub]

#         plt.figure()
#         plt.subplot(2,2,1)
#         sns.boxplot(x='labels',y='streamlengths',data=sub_df)

#         plt.subplot(2,2,2)
#         sns.boxplot(x ='labels',y='GI',data=sub_df)

#         plt.subplot(2,2,3)
#         sns.boxplot(x='labels',y='qMap',data=sub_df)

#         plt.tight_layout()
#         plt.savefig(os.path.join('output',sub+'_boxplot.png'))


#         plt.figure()
        
#         plt.subplot(2,2,1)
#         sns.lineplot(x='x_label',y='streamlengths',hue='labels',data =sub_df)

#         plt.subplot(2,2,2)
#         sns.lineplot(x='x_label',y='GI',hue='labels',data =sub_df)
        
#         plt.subplot(2,2,3)
#         sns.lineplot(x='x_label',y='qMap',hue='labels',data =sub_df)

#         plt.tight_layout()
#         plt.savefig(os.path.join('output',sub+'_ap.png'))

for sub_count in range(len(snakemake.input)):
    if os.path.isfile(snakemake.output[0]):
        pickle_df = pd.read_pickle(snakemake.output[0])
        pickle_sub = pd.read_pickle(snakemake.input[sub_count])
        pickle_concat = pd.concat([pickle_df,pickle_sub])
        pickle_concat.to_pickle(snakemake.output[0])
    else:
        pickle_df = pd.read_pickle(snakemake.input[0])
        pickle_df.to_pickle(snakemake.output[0])

    # visualize_subj(pickle_df)

# pickle_to_csv = pd.read_pickle(snakemake.output[0])
# pickle_to_csv.to_csv(snakemake.output[1],index=False)