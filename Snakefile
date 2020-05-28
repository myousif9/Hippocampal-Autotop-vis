from os.path import join
import pandas as pd
from glob import glob

configfile: 'config.yaml'

df = pd.read_table(config['participant_tsv'])
subjects = df.participant_id.to_list()
singularity_img = config["singularity"]

wildcard_constraints:
    subject="[0-9]+"

rule all:
    input: 
        expand("output/{subject}_thick_unfold.png", subject = subjects),
        expand("output/{subject}_GI_unfold.png", subject = subjects),
        expand("output/{subject}_qmap_unfold.png", subject = subjects),
        
        expand("output/{subject}_unfolded.npz", subject = subjects),
        expand("output/{subject}_unfold_data.pkl", subject = subjects),
        
        expand('output/{subject}_AP_viridis.gif', subject = subjects),
        expand('output/{subject}_IO_viridis.gif', subject = subjects),
        expand('output/{subject}_PD_viridis.gif', subject = subjects),

        "output/unfold_data.pkl",
        "output/unfold_data.csv"

 

rule gif_hippo:
    input: expand(join(config['input_dir'],'{{subject}}','hemi-L','coords-{coords}.nii.gz'), coords=config['coords'])
     
    params: 
        out_temp = expand('output/{{subject}}_{coords}.nii', coords=config['coords']),
        out = expand(join(config['input_dir'],'{{subject}}','hemi-L','coords-{coords}.nii'), coords=config['coords'])

    output: expand('output/{{subject}}_{coords}_viridis.gif', coords=config['coords'])

    singularity:
        singularity_img
    run:
        for i,file in enumerate(input):
            print(file)
            shell('gunzip -k -c {input} > {output}'.format(input=file,output=params.out_temp[i]))
            shell('gif_your_nifti {} --fps 30 --mode pseudocolor --size 0.5 --cmap viridis'.format(params.out_temp[i]))
            
            
rule data_extraction:
    input:
        unfold_mat = join(config['input_dir'],'{subject}/hemi-L/unfold.mat'),
        surf_mat = join(config['input_dir'],'{subject}/hemi-L/surf.mat'),
        boundary_mat = config['boundary'],
        # sub = expand("{subject}", subject = subjects)
    output: 
        unfold_npz = "output/{subject}_unfolded.npz",
        data_table = "output/{subject}_unfold_data.pkl",
        unfold_thick_img = "output/{subject}_thick_unfold.png",
        unfold_gyri_idex_img = "output/{subject}_GI_unfold.png",
        unfold_qmap_img = "output/{subject}_qmap_unfold.png"
        
    script: "scripts/dataextract.py"

rule aggregate:
    input:
        ["output/{subject}_unfold_data.pkl".format(subject=subject) for subject in subjects]
    output:
        "output/unfold_data.pkl"

    script: "scripts/aggreg_data.py"

rule visualize:
    input:
        "output/unfold_data.pkl"
    output:
        "output/unfold_data.csv"
    script: "scripts/visualize.py"