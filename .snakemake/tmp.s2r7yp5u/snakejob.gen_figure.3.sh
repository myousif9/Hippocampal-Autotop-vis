#!/bin/sh
# properties = {"type": "single", "rule": "gen_figure", "local": false, "input": ["/scratch/jdekrake/Hippocampal_AutoTop/misc/BigBrain_ManualSubfieldsUnfolded.mat", "/home/myousif9/scratch/hcp_unfolding3_jdkrek/601127/hemi-L/surf.mat"], "output": ["output/601127_hemi-L_streamlengths_unfold.png"], "wildcards": {"subject": "601127", "hemi": "L", "feature": "streamlengths"}, "params": {}, "log": [], "threads": 1, "resources": {"mem_mb": 4000}, "jobid": 3, "cluster": {}}
 cd /scratch/myousif9/snakemake_hippocampal_unfolding && \
/project/6007967/akhanf/opt/virtualenvs/snakemake/bin/python \
-m snakemake output/601127_hemi-L_streamlengths_unfold.png --snakefile /scratch/myousif9/snakemake_hippocampal_unfolding/Snakefile \
--force -j --keep-target-files --keep-remote \
--wait-for-files /scratch/myousif9/snakemake_hippocampal_unfolding/.snakemake/tmp.s2r7yp5u /scratch/jdekrake/Hippocampal_AutoTop/misc/BigBrain_ManualSubfieldsUnfolded.mat /home/myousif9/scratch/hcp_unfolding3_jdkrek/601127/hemi-L/surf.mat --latency-wait 5 \
 --attempt 1 --force-use-threads \
--wrapper-prefix https://github.com/snakemake/snakemake-wrappers/raw/ \
   --allowed-rules gen_figure --nocolor --notemp --no-hooks --nolock \
--mode 2  --use-singularity  --singularity-prefix /project/ctb-akhanf/akhanf/singularity/snakemake_containers  --singularity-args "\-e" --use-envmodules --default-resources "mem_mb=4000"  && touch /scratch/myousif9/snakemake_hippocampal_unfolding/.snakemake/tmp.s2r7yp5u/3.jobfinished || (touch /scratch/myousif9/snakemake_hippocampal_unfolding/.snakemake/tmp.s2r7yp5u/3.jobfailed; exit 1)

