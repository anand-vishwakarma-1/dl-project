# Deep Learning Project: Context-Aware Story Generation


Team:<br>
| | |
|---|---|
| Raj Ghodasara | rg4357 |
| Anand Vishwakarma | asv8775 |
| Vidya Bhagnani | vb2356 |

Project report - [Deep_Learning_Project_Report.pdf](Deep_Learning_Project_Report.pdf)

# 
# GPT - 2 Fine-tuning

GPT-2 Fine-tuning
```
Usage: python run_lm_finetuning.py [--output_dir=PATH/TO/OUTPUT/DIR/] 
    [--model_type=MODEL_TYPE] 
    [--model_name_or_path=PATH/TO/MODEL/] 
    [--do_train ]
    [--train_data_file=PATH/TO/TRAINING/DATA/] 
    [--do_eval ]
    [--eval_data_file=PATH/TO/EVAL/DATA/] 
    [--overwrite_output_dir ]
    [--num_train_epochs=NUM_EPOCHS]
    [--block_size=BLOCK_SIZE]
    [--save_steps=SAVE_EVERY_STEPS]
    [--logging_steps=LOG_EVERY_STEPS]
```

GPT-2 Generation using fine-tuned model
```
Usage: python run_generation.py 
    [--model_type MODEL_TYPE] 
    [--model_name_or_path=PATH/TO/MODEL/] 
    [--length=OUTPUT_LENGTH]
```

# Example usage
```
python run_lm_finetuning.py 
    --output_dir="/scratch/rg4357/dl/dialogrepo/Output_extended_1024_block/" 
    --model_type=gpt2 
    --model_name_or_path=gpt2 
    --do_train 
    --train_data_file="/scratch/rg4357/dl/dialogrepo/examples/input_data/train_GOT.txt" 
    --do_eval 
    --eval_data_file="/scratch/rg4357/dl/dialogrepo/examples/input_data/val_GOT.txt" 
    --overwrite_output_dir 
    --num_train_epochs=30 
    --block_size=1024 
    --save_steps=200 
    --logging_steps=200
```
Fine-tune a default GPT-2 model with training data train_GOT.txt and evaluation data eval_GOT.txt for 30 epochs and block size 1024, saving and logging every 200 steps

```
python run_generation.py 
    --model_type=gpt2 
    --model_name_or_path="/scratch/rg4357/dl/dialogrepo/Output_1024_block_extended/FT_512_select_dialogues/checkpoint-4000/" 
    --length=300
```
Use a fine-tuned GPT-2 model to generate a text of length 300.
#
# DC-TTS
Environment Requirements
```
tensorlfow=1.15
cudatoolkit=10.0
cudnn=7.6
```
Change hyperparameters.py file to set dataset and model paths

To create custom dataset from captioned video use [data_prep.py](data_prep.py), change output path and json prefixes accordingly.<br>
Sample raw data and processed data can be found in the drive link provided above.

Pre-process custom dataset
```
python prepo.py
```
Train model, get pretrained model trained on LJ speech from [this](https://www.dropbox.com/s/1oyipstjxh2n5wo/LJ_logdir.tar?dl=0) link. 
```
python train.py 1
python train.py 2
```
Get sample outputs
```
python synthesize.py
```
#
# Final results
Use [step_2-3.ipynb](step_2-3.ipynb) on get final result using a sample [prompt](prompt1.txt) provided which is generated from our step 1.

## Final sample
[sample.mp4](sample.mp4)
<video width="320" height="240" controls>
  <source src="sample.mp4" type="video/mp4">
</video>

# Github links referred
[Kyubyong/dc_tts](https://github.com/Kyubyong/dc_tts)<br>
[Rudrabha/Wav2Lip](https://github.com/Rudrabha/Wav2Lip)

# Citation
```
@inproceedings{10.1145/3394171.3413532,
author = {Prajwal, K R and Mukhopadhyay, Rudrabha and Namboodiri, Vinay P. and Jawahar, C.V.},
title = {A Lip Sync Expert Is All You Need for Speech to Lip Generation In the Wild},
year = {2020},
isbn = {9781450379885},
publisher = {Association for Computing Machinery},
address = {New York, NY, USA},
url = {https://doi.org/10.1145/3394171.3413532},
doi = {10.1145/3394171.3413532},
booktitle = {Proceedings of the 28th ACM International Conference on Multimedia},
pages = {484–492},
numpages = {9},
keywords = {lip sync, talking face generation, video generation},
location = {Seattle, WA, USA},
series = {MM '20}
}
```

