#!/bin/bash
# bash script showing how to switch between conda envs

source /root/miniconda/etc/profile.d/conda.sh
conda activate recycler
echo recycler
python -V
conda deactivate
echo base
python -V
