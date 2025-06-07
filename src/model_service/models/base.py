from abc import ABC, abstractmethod
from typing import Dict, Any, List, Optional
from pydantic import BaseModel

class ChatMessage(BaseModel):
    role: str
    content: str

class ChatRequest(BaseModel):
    model_name: str
    messages: List[ChatMessage]
    max_tokens: Optional[int] = 32768
    enable_thinking: Optional[bool] = True

class BaseLLMService(ABC):
    @abstractmethod
    def load_model(self):
        """Load the model and tokenizer"""
        pass

    @abstractmethod
    async def generate_response(self, chat_request: ChatRequest) -> Dict[str, Any]:
        """Generate response for the given chat messages"""
        pass