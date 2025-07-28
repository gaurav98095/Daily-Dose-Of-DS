# Step 1: Load model
# pip install unsloth
from unsloth import FastLanguageModel
from unsloth import FastModel
import torch

MODEL = "unsloth/gemma-3-4b-it"

model, tokenizer = FastLanguageModel.from_pretrained(
    model_name = MODEL,
    max_seq_length = 2048,
    dtype = None,
    load_in_4bit = True,
    full_finetuning = False,
)

# Step 2: Define LoRA config
model = FastModel.get_peft_model(
    model,
    finetune_vision_layers = False,
    finetune_language_layers = True,
    finetune_attention_modules = True,
    finetune_mlp_modules = True,
    r = 4,
    lora_alpha = 4,
    lora_dropout = 0,
    bias = "none",
)

# Step 3: Prepare dataset
from datasets import load_dataset
from unsloth import to_sharegpt
from unsloth.chat_templates import standardize_data_formats

dataset = load_dataset("mlabonne/FineTome-100k", split = "train")
dataset = standardize_data_formats(dataset)

def apply_chat_template(examples):
    texts = tokenizer.apply_chat_template(examples["conversations"])
    return {"text": texts}

dataset = dataset.map(apply_chat_template, batched=True)

# Step 4: Define Trainer
from trl import SFTTrainer, SFTConfig

trainer = SFTTrainer(
    model = model,
    tokenizer = tokenizer,
    train_dataset = dataset,
    args = SFTConfig(
        per_device_train_batch_size = 2,
        gradient_accumulation_steps = 4,
        max_steps = 60,
        learning_rate = 2e-4,
        optim = "adamw_8bit",
        weight_decay = 0.01,
    )
)


# Step 5: Train
trainer_stats = trainer.train()

# Step 6: Run Locally
messages = [{
    "role": "user",
    "content": [{
        "type": "text",
        "text": "Continue the sequence: 1, 1, 2, 3, 5, 8,"
    }]
}]

# Format into chat prompt
text = tokenizer.apply_chat_template(
    messages,
    add_generation_prompt = True
)

# Generate response
outputs = model.generate(
    **tokenizer([text], return_tensors="pt").to("cuda"),
    max_new_tokens = 64,
    temperature = 1.0,
    top_p = 0.95,
    top_k = 64,
)

# Decode output
response = tokenizer.batch_decode(outputs)
print(response[0])
