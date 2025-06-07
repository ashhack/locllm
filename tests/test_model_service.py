import pytest
from fastapi.testclient import TestClient
from src.model_service.main import app
from src.model_service.models.base import ChatRequest, Message

client = TestClient(app)

def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}

def test_list_models():
    response = client.get("/models")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert "qwen" in data  # Since we have Qwen model implemented

def test_generate_text_success():
    chat_request = {
        "messages": [
            {
                "role": "user",
                "content": "What is Python?"
            }
        ],
        "max_tokens": 100,
        "enable_thinking": True
    }
    
    response = client.post("/generate", json=chat_request)
    assert response.status_code == 200
    data = response.json()
    assert "content" in data
    assert "thinking_content" in data
    assert "model" in data
    assert "status" in data
    assert data["status"] == "success"

def test_generate_text_invalid_request():
    # Test with missing messages
    invalid_request = {
        "max_tokens": 100,
        "enable_thinking": True
    }
    
    response = client.post("/generate", json=invalid_request)
    assert response.status_code == 422  # Validation error

def test_generate_text_empty_messages():
    chat_request = {
        "messages": [],
        "max_tokens": 100,
        "enable_thinking": True
    }
    
    response = client.post("/generate", json=chat_request)
    assert response.status_code == 400
    assert "error" in response.json()

def test_generate_text_invalid_max_tokens():
    chat_request = {
        "messages": [
            {
                "role": "user",
                "content": "Hello"
            }
        ],
        "max_tokens": -1,  # Invalid token count
        "enable_thinking": True
    }
    
    response = client.post("/generate", json=chat_request)
    assert response.status_code == 422  # Validation error

def test_generate_text_long_conversation():
    chat_request = {
        "messages": [
            {
                "role": "user",
                "content": "Hi"
            },
            {
                "role": "assistant",
                "content": "Hello! How can I help you today?"
            },
            {
                "role": "user",
                "content": "Tell me about Python"
            }
        ],
        "max_tokens": 100,
        "enable_thinking": True
    }
    
    response = client.post("/generate", json=chat_request)
    assert response.status_code == 200
    data = response.json()
    assert "content" in data
    assert "thinking_content" in data

def test_model_not_found():
    # Test accessing a non-existent model endpoint
    response = client.get("/models/nonexistent")
    assert response.status_code == 404

# Optional: Add mock tests if you want to test without loading the actual model
@pytest.mark.skip(reason="Requires mock implementation")
def test_generate_text_with_mock_model():
    # TODO: Implement mock test cases that don't require loading the actual model
    pass