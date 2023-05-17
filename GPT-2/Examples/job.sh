#!/bin/bash
#SBATCH --job-name=fine_tune
#SBATCH --nodes=1
#SBATCH --cpus-per-task=5
#SBATCH --mem=64GB
#SBATCH --time=03:00:00
#SBATCH --output="block_extended_1024.txt"
#SBATCH --mail-type=END
#SBATCH --mail-user=rg4357@nyu.edu
#SBATCH --gres=gpu:rtx8000:1
#SBATCH --account=class
#SBATCH --priority=4294967293

module purge

singularity exec --nv --overlay /scratch/rg4357/my_env/project.ext3:ro /scratch/work/public/singularity/cuda11.6.124-cudnn8.4.0.27-devel-ubuntu20.04.4.sif \
	/bin/bash -c 'source /ext3/env.sh;
    python run_lm_finetuning.py --output_dir="/scratch/rg4357/dl/dialogrepo/Output_extended_1024_block/" --model_type=gpt2 --model_name_or_path=gpt2 --do_train --train_data_file="/scratch/rg4357/dl/dialogrepo/examples/input_data/train_GOT.txt" --do_eval --eval_data_file="/scratch/rg4357/dl/dialogrepo/examples/input_data/val_GOT.txt" --overwrite_output_dir --num_train_epochs=30 --block_size=1024 --save_steps=200 --logging_steps=200'