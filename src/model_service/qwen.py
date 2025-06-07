import os
import json

from transformers import AutoModelForCausalLM, AutoTokenizer
from transformers.tokenization_utils import PreTrainedTokenizer
from transformers.modeling_utils import PreTrainedModel
from fastapi import HTTPException
from typing import Dict, Any
from base import BaseLLMService, ChatRequest

class QwenService(BaseLLMService):
    def __init__(self):
        self.model_path = os.path.join("..", "..", "models", "Qwen3-0.6B")
        self.load_model()

    def load_model(self):
        self.tokenizer: PreTrainedTokenizer = AutoTokenizer.from_pretrained(self.model_path)  # type: ignore
        self.model = AutoModelForCausalLM.from_pretrained(  # type: ignore
            self.model_path,
            torch_dtype="auto",
            device_map="auto"
        )

    async def generate_response(self, chat_request: ChatRequest) -> Dict[str, Any]:
        try:
            messages = [{"role": msg.role, "content": msg.content} for msg in chat_request.messages]
            
            text = self.tokenizer.apply_chat_template(
                messages,
                tokenize=False,
                add_generation_prompt=True,
                enable_thinking=chat_request.enable_thinking
            )
            model_inputs = self.tokenizer([text], return_tensors="pt").to(self.model.device)

            generated_ids = self.model.generate(
                **model_inputs,
                max_new_tokens=chat_request.max_tokens
            )
            output_ids = generated_ids[0][len(model_inputs.input_ids[0]):].tolist()

            try:
                index = len(output_ids) - output_ids[::-1].index(151668)
            except ValueError:
                index = 0

            thinking_content = self.tokenizer.decode(output_ids[:index], skip_special_tokens=True).strip("\n")
            content = self.tokenizer.decode(output_ids[index:], skip_special_tokens=True).strip("\n")

            return {
                "thinking_content": thinking_content,
                "content": content,
                "model": "qwen",
                "status": "success"
            }
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Qwen model generation failed: {str(e)}")