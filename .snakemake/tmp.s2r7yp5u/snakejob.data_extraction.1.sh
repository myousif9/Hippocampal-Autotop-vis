#!/bin/sh
# properties = {"type": "single", "rule": "data_extraction", "local": false, "input": ["/scratch/jdekrake/Hippocampal_AutoTop/misc/BigBrain_ManualSubfieldsUnfolded.mat", "/home/myousif9/scratch/hcp_unfolding3_jdkrek/601127/hemi-L/surf.mat"], "output": ["output/601127_unfolded.npz", "output/601127_unfold_data.pkl"], "wildcards": {"subject": "601127"}, "params": {"hemi": ["L"]}, "log": [], "threads": 1, "resources": {"mem_mb": 4000}, "jobid": 1, "cluster": {}}
 cd /scratch/myousif9/snakemake_hippocampal_unfolding && \
/project/6007967/akhanf/opt/virtualenvs/snakemake/bin/python \
-m snakemake output/601127_unfolded.npz --snakefile /scratch/myousif9/snakemake_hippocampal_unfolding/Snakefile \
--force -j --keep-target-files --keep-remote \
--wait-for-files /scratch/myousif9/snakemake_hippocampal_unfolding/.snakemake/tmp.s2r7yp5u /scratch/jdekrake/Hippocampal_AutoTop/misc/BigBrain_ManualSubfieldsUnfolded.mat /home/myousif9/scratch/hcp_unfolding3_jdkrek/601127/hemi-L/surf.mat --latency-wait 5 \
 --attempt 1 --force-use-threads \
--wrapper-prefix https://github.com/snakemake/snakemake-wrappers/raw/ \
   --allowed-rules data_extraction --nocolor --notemp --no-hooks --nolock \
--mode 2  --use-singularity  --singularity-prefix /project/ctb-akhanf/akhanf/singularity/snakemake_containers  --singularity-args "\-e" --use-envmodules --default-resources "mem_mb=4000"  && touch /scratch/myousif9/snakemake_hippocampal_unfolding/.snakemake/tmp.s2r7yp5u/1.jobfinished || (touch /scratch/myousif9/snakemake_hippocampal_unfolding/.snakemake/tmp.s2r7yp5u/1.jobfailed; exit 1)

