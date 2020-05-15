from os.path import join
import pandas as pd

configfile: 'config.yaml'

df = pd.read_table(config['participant_tsv'])
subjects = df.participant_id.to_list()

wildcard_constraints:
    subject="[0-9]+"

rule all:
    input: 'output/100610_unfolded.png'

rule gen_figure:
    input:
        unfold_mat = join(config['input_dir'],'100610/hemi-L/unfold.mat'),
        surf_mat = join(config['input_dir'],'100610/hemi-L/surf.mat'),
        boundary_mat = config['boundary']
    output: 'output/100610_unfolded.png'
    script: 'scripts/gen_figure.py'