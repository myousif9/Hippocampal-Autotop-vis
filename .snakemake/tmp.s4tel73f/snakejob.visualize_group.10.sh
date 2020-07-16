#!/bin/sh
# properties = {"type": "single", "rule": "visualize_group", "local": false, "input": ["output/unfold_data.pkl"], "output": ["output/601127_hemi-L_streamlengths_violinplot_group.png"], "wildcards": {"subject": "601127", "hemi": "L", "feature": "streamlengths", "plot": "violinplot"}, "params": {}, "log": [], "threads": 1, "resources": {"mem_mb": 4000}, "jobid": 10, "cluster": {}}
 cd /scratch/myousif9/snakemake_hippocampal_unfolding && \
/project/6007967/akhanf/opt/virtualenvs/snakemake/bin/python \
-m snakemake output/601127_hemi-L_streamlengths_violinplot_group.png --snakefile /scratch/myousif9/snakemake_hippocampal_unfolding/Snakefile \
--force -j --keep-target-files --keep-remote \
--wait-for-files /scratch/myousif9/snakemake_hippocampal_unfolding/.snakemake/tmp.s4tel73f output/unfold_data.pkl --latency-wait 5 \
 --attempt 1 --force-use-threads \
--wrapper-prefix https://github.com/snakemake/snakemake-wrappers/raw/ \
   --allowed-rules visualize_group --nocolor --notemp --no-hooks --nolock \
--mode 2  --use-singularity  --singularity-prefix /project/ctb-akhanf/akhanf/singularity/snakemake_containers  --singularity-args "\-e" --use-envmodules --default-resources "mem_mb=4000"  && touch /scratch/myousif9/snakemake_hippocampal_unfolding/.snakemake/tmp.s4tel73f/10.jobfinished || (touch /scratch/myousif9/snakemake_hippocampal_unfolding/.snakemake/tmp.s4tel73f/10.jobfailed; exit 1)

