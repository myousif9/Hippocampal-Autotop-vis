#!/bin/sh
# properties = {"type": "single", "rule": "all", "local": true, "input": ["output/601127_unfolded.npz", "output/601127_unfold_data.pkl", "output/601127_hemi-L_GI_unfold.png", "output/601127_hemi-L_streamlengths_unfold.png", "output/unfold_data.pkl", "output/601127_hemi-L_AP_viridis.gif", "output/601127_hemi-L_IO_viridis.gif", "output/601127_hemi-L_PD_viridis.gif", "output/601127_hemi-L_GI_violinplot_group.png", "output/601127_hemi-L_GI_lineplot_group.png", "output/601127_hemi-L_streamlengths_violinplot_group.png", "output/601127_hemi-L_streamlengths_lineplot_group.png", "output/601127_hemi-L_qMap_violinplot_group.png", "output/601127_hemi-L_qMap_lineplot_group.png"], "output": [], "wildcards": {}, "params": {}, "log": [], "threads": 1, "resources": {"mem_mb": 4000}, "jobid": 0, "cluster": {}}
 cd /scratch/myousif9/snakemake_hippocampal_unfolding && \
/project/6007967/akhanf/opt/virtualenvs/snakemake/bin/python \
-m snakemake all --snakefile /scratch/myousif9/snakemake_hippocampal_unfolding/Snakefile \
--force -j --keep-target-files --keep-remote \
--wait-for-files /scratch/myousif9/snakemake_hippocampal_unfolding/.snakemake/tmp.s4tel73f output/601127_unfolded.npz output/601127_unfold_data.pkl output/601127_hemi-L_GI_unfold.png output/601127_hemi-L_streamlengths_unfold.png output/unfold_data.pkl output/601127_hemi-L_AP_viridis.gif output/601127_hemi-L_IO_viridis.gif output/601127_hemi-L_PD_viridis.gif output/601127_hemi-L_GI_violinplot_group.png output/601127_hemi-L_GI_lineplot_group.png output/601127_hemi-L_streamlengths_violinplot_group.png output/601127_hemi-L_streamlengths_lineplot_group.png output/601127_hemi-L_qMap_violinplot_group.png output/601127_hemi-L_qMap_lineplot_group.png --latency-wait 5 \
 --attempt 1 --force-use-threads \
--wrapper-prefix https://github.com/snakemake/snakemake-wrappers/raw/ \
   --allowed-rules all --nocolor --notemp --no-hooks --nolock \
--mode 2  --use-singularity  --singularity-prefix /project/ctb-akhanf/akhanf/singularity/snakemake_containers  --singularity-args "\-e" --use-envmodules --default-resources "mem_mb=4000"  && touch /scratch/myousif9/snakemake_hippocampal_unfolding/.snakemake/tmp.s4tel73f/0.jobfinished || (touch /scratch/myousif9/snakemake_hippocampal_unfolding/.snakemake/tmp.s4tel73f/0.jobfailed; exit 1)

