#!/bin/sh
# properties = {"type": "group", "groupid": "quality-control", "local": false, "input": ["/home/myousif9/scratch/hcp_unfolding3_jdkrek/601127/hemi-L/coords-IO.nii.gz"], "output": ["output/601127_hemi-L_IO_viridis.gif"], "threads": 1, "resources": {"mem_mb": 4000}, "jobid": "d2e4dd36-14a6-5506-b5dd-c99749b79f3b", "cluster": {}}
 cd /scratch/myousif9/snakemake_hippocampal_unfolding && \
/project/6007967/akhanf/opt/virtualenvs/snakemake/bin/python \
-m snakemake output/601127_hemi-L_IO_viridis.gif --snakefile /scratch/myousif9/snakemake_hippocampal_unfolding/Snakefile \
--force -j --keep-target-files --keep-remote \
--wait-for-files /scratch/myousif9/snakemake_hippocampal_unfolding/.snakemake/tmp.s2r7yp5u /home/myousif9/scratch/hcp_unfolding3_jdkrek/601127/hemi-L/coords-IO.nii.gz --latency-wait 5 \
 --attempt 1  \
--wrapper-prefix https://github.com/snakemake/snakemake-wrappers/raw/ \
   --allowed-rules gif_hippo --nocolor --notemp --no-hooks --nolock \
--mode 2  --use-singularity  --singularity-prefix /project/ctb-akhanf/akhanf/singularity/snakemake_containers  --singularity-args "\-e" --use-envmodules --default-resources "mem_mb=4000"  && touch /scratch/myousif9/snakemake_hippocampal_unfolding/.snakemake/tmp.s2r7yp5u/d2e4dd36-14a6-5506-b5dd-c99749b79f3b.jobfinished || (touch /scratch/myousif9/snakemake_hippocampal_unfolding/.snakemake/tmp.s2r7yp5u/d2e4dd36-14a6-5506-b5dd-c99749b79f3b.jobfailed; exit 1)

