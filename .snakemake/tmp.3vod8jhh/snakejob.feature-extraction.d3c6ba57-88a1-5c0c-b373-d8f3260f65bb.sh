#!/bin/sh
# properties = {"type": "group", "groupid": "feature-extraction", "local": false, "input": ["output/601127_unfold_data.pkl"], "output": ["output/unfold_data.pkl"], "threads": 1, "resources": {"mem_mb": 4000}, "jobid": "d3c6ba57-88a1-5c0c-b373-d8f3260f65bb", "cluster": {}}
 cd /scratch/myousif9/snakemake_hippocampal_unfolding && \
/project/6007967/akhanf/opt/virtualenvs/snakemake/bin/python \
-m snakemake output/unfold_data.pkl --snakefile /scratch/myousif9/snakemake_hippocampal_unfolding/Snakefile \
--force -j --keep-target-files --keep-remote \
--wait-for-files /scratch/myousif9/snakemake_hippocampal_unfolding/.snakemake/tmp.3vod8jhh output/601127_unfold_data.pkl --latency-wait 5 \
 --attempt 1  \
--wrapper-prefix https://github.com/snakemake/snakemake-wrappers/raw/ \
   --allowed-rules aggregate --nocolor --notemp --no-hooks --nolock \
--mode 2  --use-singularity  --singularity-prefix /project/ctb-akhanf/akhanf/singularity/snakemake_containers  --singularity-args "\-e" --use-envmodules --default-resources "mem_mb=4000"  && touch /scratch/myousif9/snakemake_hippocampal_unfolding/.snakemake/tmp.3vod8jhh/d3c6ba57-88a1-5c0c-b373-d8f3260f65bb.jobfinished || (touch /scratch/myousif9/snakemake_hippocampal_unfolding/.snakemake/tmp.3vod8jhh/d3c6ba57-88a1-5c0c-b373-d8f3260f65bb.jobfailed; exit 1)

