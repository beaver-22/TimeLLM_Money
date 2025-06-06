import torch
from transformers import LlamaTokenizer, LlamaModel

model_id = "meta-llama/Llama-3.1-8B"

# 다운로드 및 캐시
model = LlamaModel.from_pretrained(
    model_id, 
    device_map="auto", 
    torch_dtype=torch.bfloat16
)
tokenizer = LlamaTokenizer.from_pretrained(model_id)

# 로컬에 저장
model.save_pretrained("./models/llama-3.1-8b/")
tokenizer.save_pretrained("./models/llama-3.1-8b/")