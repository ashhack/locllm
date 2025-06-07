from fastapi import FastAPI, HTTPException
from base import ChatRequest
from model_factory import ModelFactory

app = FastAPI()

@app.post("/generate")
async def generate(chat_request: ChatRequest):
    """Endpoint for generating responses using specified model"""
    try:
        model_service = ModelFactory.get_model(chat_request.model_name.lower())
        return await model_service.generate_response(chat_request)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))