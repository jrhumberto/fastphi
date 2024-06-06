from transformers import AutoTokenizer, AutoModelForCausalLM
import torch
import os

hf_cache_folder = './huggingface_cache/'
os.makedirs(hf_cache_folder, exist_ok=True)

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

model_id = "microsoft/Phi-3-mini-128k-instruct"
tokenizer = AutoTokenizer.from_pretrained(model_id, cache_dir=hf_cache_folder, trust_remote_code=True)
model = AutoModelForCausalLM.from_pretrained(model_id, cache_dir=hf_cache_folder, device_map="auto", trust_remote_code=True)
## <BOS_TOKEN><|START_OF_TURN_TOKEN|><|USER_TOKEN|>Hello, how are you?<|END_OF_TURN_TOKEN|><|START_OF_TURN_TOKEN|><|CHATBOT_TOKEN|>


async def get_answer_from_llm(question: str = None):
    # Format message with the command-r chat template
    messages = [{"role": "user", "content": f"{question}"}]
    input_ids = tokenizer.apply_chat_template(messages, tokenize=True, add_generation_prompt=True, return_tensors="pt")
    gen_tokens = model.generate(
        input_ids.to(device),
        max_new_tokens=100,
        do_sample=True,
        temperature=0.3,
        )

    gen_text = tokenizer.decode(gen_tokens[0])
    return gen_text
