accelerate launch ./amused/training/train_amused.py \
    --output_dir output \
    --mixed_precision fp16 \
    --report_to wandb \
    --use_lora \
    --pretrained_model_name_or_path amused/amused-256 \
    --train_batch_size 1 \
    --lr_scheduler constant \
    --learning_rate 1e-3 \
    --validation_prompts \
        'A chihuahua walking on the street in [V] style' \
        'A banana on the table in [V] style' \
        'A church on the street in [V] style' \
        'A tabby cat walking in the forest in [V] style' \
    --instance_data_image './amused/training/A mushroom in [V] style.png' \
    --max_train_steps 100000 \
    --checkpointing_steps 500 \
    --validation_steps 100 \
    --resolution 256 \
    --lora_alpha 1