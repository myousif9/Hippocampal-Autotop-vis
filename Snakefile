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
        
        expand('output/{subject}_ap_viridis.gif', subject = subjects),
        expand('output/{subject}_io_viridis.gif', subject = subjects),
        expand('output/{subject}_pd_viridis.gif', subject = subjects),

        "output/unfold_data.pkl"

        # expand(join(config['input_dir'],'{subject}','hemi-L','coords-AP.nii'), subject = subjects),
        # expand(join(config['input_dir'],'{subject}','hemi-L','coords-IO.nii'), subject = subjects),
        # expand(join(config['input_dir'],'{subject}','hemi-L','coords-PD.nii'), subject = subjects),

        # expand('output/{subject}_ap.nii', subject = subjects),
        # expand('output/{subject}_io.nii', subject = subjects),
        # expand('output/{subject}_pd.nii', subject = subjects),
        #expand('log/gif_hippo_{subject}.log', subject = subjects)
        # expand(join(config['input_dir'],'{subject},coords*.nii.gz'),)

rule gif_hippo:
    input:
        qc_ap = join(config['input_dir'],'{subject}','hemi-L','coords-AP.nii.gz'),
        qc_io = join(config['input_dir'],'{subject}','hemi-L','coords-IO.nii.gz'),
        qc_pd = join(config['input_dir'],'{subject}','hemi-L','coords-PD.nii.gz'),

    params:
        ap_out_temp = 'output/{subject}_ap.nii',
        io_out_temp = 'output/{subject}_io.nii',
        pd_out_temp = 'output/{subject}_pd.nii',

        ap_temp = join(config['input_dir'],'{subject}','hemi-L','coords-AP.nii'),
        io_temp = join(config['input_dir'],'{subject}','hemi-L','coords-IO.nii'),
        pd_temp = join(config['input_dir'],'{subject}','hemi-L','coords-PD.nii'),
    
    output:
        ap_gif = 'output/{subject}_ap_viridis.gif',
        io_gif = 'output/{subject}_io_viridis.gif',
        pd_gif = 'output/{subject}_pd_viridis.gif',

    log: 'logs/gif_hippo_{subject}.log'
    singularity:
        singularity_img
    shell:
        """
            (gunzip -k {input.qc_ap} &&
            mv {params.ap_temp} {params.ap_out_temp} &&
            gif_your_nifti {params.ap_out_temp} --fps 30 --mode pseudocolor --size 0.5 --cmap viridis)  &> {log}
           
            (gunzip -k {input.qc_io} &&
            mv {params.io_temp} {params.io_out_temp} &&
            gif_your_nifti {params.io_out_temp} --fps 30 --mode pseudocolor --size 0.5 --cmap viridis)  &> {log}

            (gunzip -k {input.qc_pd} &&
            mv {params.pd_temp} {params.pd_out_temp}
            gif_your_nifti {params.pd_out_temp} --fps 30 --mode pseudocolor --size 0.5 --cmap viridis)  &> {log}
        """
rule unfolded_plotting_data_extraction:
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
        
    script: "scripts/genfigure_dataextract.py"

rule aggregate:
    input:
        ["output/{subject}_unfold_data.pkl".format(subject=subject) for subject in subjects]
    output:
        "output/unfold_data.pkl"

    script: "scripts/aggreg_data.py"
