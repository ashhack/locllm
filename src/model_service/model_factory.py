from typing import Dict, Type
from base import BaseLLMService
from qwen import QwenService

class ModelFactory:
    _models: Dict[str, Type[BaseLLMService]] = {
        "qwen": QwenService
    }
    _instances: Dict[str, BaseLLMService] = {}

    @classmethod
    def get_model(cls, model_name: str) -> BaseLLMService:
        if model_name not in cls._instances:
            if model_name not in cls._models:
                raise ValueError(f"Model {model_name} not supported")
            cls._instances[model_name] = cls._models[model_name]()
        return cls._instances[model_name]