from os.path import join
import pandas as pd
from glob import glob

configfile: 'config.yaml'

df = pd.read_table(config['participant_tsv'])
subjects = df.participant_id.to_list()

wildcard_constraints:
    subject="[0-9]+"

rule all:
    input: 
        expand("output/{subject}_unfolded.png", subject = subjects),
        expand("output/{subject}_unfolded.npz", subject = subjects),
        expand("output/{subject}_unfold_data.pkl", subject = subjects),

rule unfolded_plotting_data_extraction:
    input:
        unfold_mat = join(config['input_dir'],'{subject}/hemi-L/unfold.mat'),
        surf_mat = join(config['input_dir'],'{subject}/hemi-L/surf.mat'),
        boundary_mat = config['boundary'],
        # sub = expand("{subject}", subject = subjects)
    output: 
        unfold_img = "output/{subject}_unfolded.png",
        unfold_npz = "output/{subject}_unfolded.npz",
        data_table = "output/{subject}_unfold_data.pkl"
    script: "scripts/genfigure_dataextract.py"

# rule extract_data:
#     input:
#         unfold_mat = join(config['input_dir'],'{subject}/hemi-L/unfold.mat')
#         surf_mat = join(config['input_dir'],'{subject}/hemi-L/surf.mat')
#         boundary_mat = config['boundary'],
#         subs = subjects
#     output: 
#         thickness = 'output/{subject}_thickness.csv',
#         gyrification = 'output/{subject}_gyrification.csv'
#     script: 
#         'scripts/gen_data_table.py'