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