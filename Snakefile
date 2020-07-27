from os.path import join
import pandas as pd

configfile: 'config.yaml'

df = pd.read_table(config['participant_tsv'])
subjects = df.participant_id.to_list()
singularity_img = config['singularity']


wildcard_constraints:
    subject="[A-Za-z0-9]+"

rule all:
    input:         
        expand("output/sub-{subject}_unfolded.npz", subject = subjects),
        expand("output/sub-{subject}_unfold_data.pkl", subject = subjects),
        expand("output/sub-{subject}_hemi-{hemi}_{feature}_unfold.png", subject=subjects, hemi=config['hemi'], feature=config['features']),
        "output/unfold_data.pkl",
        "output/unfold_data.csv",
#        expand('output/sub-{subject}_hemi-{hemi}_{coords}_viridis.gif', subject = subjects, hemi=config['hemi'], coords=config['coords']),
        expand("output/sub-{subject}_hemi-{hemi}_{feature}_{plot}_group.png",subject=subjects,hemi=config['hemi'],feature=['GI','streamlengths','qMap'],plot =['violinplot','lineplot']),
        # "report.html"

rule gif_hippo:
    input: join(config['input_dir'],'sub-{subject}','hemi-{hemi}','coords-{coords}.nii.gz'),

    params: 
        out_temp = 'output/sub-{subject}_hemi-{hemi}_{coords}.nii',
        # out = join(config['input_dir'],'{subject}','hemi-{hemi}','coords-{coords}.nii'),
    output: report('output/sub-{subject}_hemi-{hemi}_{coords}_viridis.gif',category="Quality control")
    group: "quality-control"
    singularity:
        singularity_img
    shell:
        """
        gunzip -k -c {input} > {params};
        gif_your_nifti {params} --fps 30 --mode pseudocolor --size 0.5 --cmap viridis
        """
    # run:
    #     print(input)
    #     for i,file in enumerate(input):
            
    #         shell('gunzip -k -c {input} > {output}'.format(input=file,output=params.out_temp))
    #         shell('gif_your_nifti {} --fps 30 --mode pseudocolor --size 0.5 --cmap viridis'.format(params.out_temp))

    

rule data_extraction:
    input:
        boundary_mat = config['boundary'],
        unfold_mat = expand(join(config['input_dir'],'sub-{{subject}}/hemi-{hemi}/{mat}.mat'),hemi=config['hemi'], mat=config['unfold_mat']),
    params:
        hemi = config['hemi']
    output: 
        unfold_npz = "output/sub-{subject}_unfolded.npz",
        data_table = "output/sub-{subject}_unfold_data.pkl",
    conda: "env/hippvis.yml"
    script: "scripts/dataextract.py"

rule gen_figure:
    input:
        boundary_mat = config['boundary'],
        unfold_mat = expand(join(config['input_dir'],'sub-{{subject}}/hemi-{{hemi}}/{mat}.mat'),mat=config['unfold_mat']),
    params:
        cmap=config['cmap']
    output: report("output/sub-{subject}_hemi-{hemi}_{feature}_unfold.png",category="Unfolded maps")
    conda: "env/hippvis.yml"
    script: "scripts/genfigure.py"

rule aggregate:
    input:
        ["output/sub-{subject}_unfold_data.pkl".format(subject=subject) for subject in subjects]
    output:
        "output/unfold_data.pkl"
    group: "feature-extraction"
    conda: "env/hippvis.yml"
    script: "scripts/aggreg_data.py"

rule pickle_to_csv:
    input:  "output/unfold_data.pkl"
    output: "output/unfold_data.csv"
    run:
        pkl_df = pd.read_pickle(input[0])
        pkl_df.to_csv(output[0])

rule visualize_group:
    input: "output/unfold_data.pkl"
    output: 
        violinplot = report("output/sub-{subject}_hemi-{hemi}_{feature}_violinplot_group.png",category="Group plots"),
        lineplot = report("output/sub-{subject}_hemi-{hemi}_{feature}_lineplot_group.png",category="Group plots")
    conda: "env/hippvis.yml"
    script:"scripts/visualize_group.py"


# rule report:
#     input:
#         qc_gifs = expand("output/sub-{subject}_hemi-{hemi}_{coords}_viridis.gif",subject=subjects,hemi=config['hemi'],coords=config['coords']),
#         unfolded_maps = expand("output/sub-{subject}_hemi-{hemi}_{feature}_unfold.png",subject=subjects,hemi=config['hemi'],feature=config['features']),
#         group_plots = expand("output/sub-{subject}_hemi-{hemi}_{feature}_{plot}_group.png",subject=subjects,hemi=config['hemi'],feature=config['features'],plot=['violinplot','lineplot']),
#     output:
#         "report.html"
#     run:
#         from snakemake.utils import report
#         report(''''
#         =============================
#         Hippocampus QC visualizations
#         =============================
#         T1_''',output[0],T1=input[0])



        
