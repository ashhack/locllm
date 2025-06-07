# Local LLM Service

This project provides a simple way to host large language models (LLMs) locally on your machine and expose them as an API service. It's designed for developers who want to build personal AI-powered applications without relying on cloud services. The service uses FastAPI for the API layer, Redis for response caching, and PostgreSQL for storing usage history.

## Project Structure

```
locllm
├── src
│   ├── model_service
│   │   ├── __init__.py
│   │   ├── main.py       # FastAPI application
│   │   └── models/
│   │       ├── base.py   # Base model interface
│   │       ├── qwen.py   # Qwen model implementation
│   │       └── model_factory.py
│   ├── database
│   │   ├── __init__.py
│   │   ├── models.py
│   │   └── postgres.py
│   ├── cache
│   │   ├── __init__.py
│   │   └── redis_manager.py
│   └── utils
│       ├── __init__.py
│       └── constants.py
├── tests
│   └── __init__.py
├── config
│   ├── __init__.py
│   └── settings.py
├── requirements.txt
├── main.py
└── README.md
```

## Setup Instructions

1. **Prerequisites**:
   - Python 3.8 or higher
   - CUDA-capable GPU (recommended) or decent CPU
   - 8GB+ RAM (16GB+ recommended)
   - Sufficient storage for models

2. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd locllm
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Download models**:
   The project comes with scripts to download supported open-source models:
   ```bash
   # Example: Download Qwen model
   python -m scripts.download_model qwen
   ```

5. **Configure the service**:
   - Update `config/settings.py` with your:
     - Model preferences (CPU/GPU, memory limits)
     - Redis cache settings
     - PostgreSQL connection details

6. **Run the service**:
   ```bash
   uvicorn src.model_service.main:app --reload
   ```

7. **Verify installation**:
   - API documentation: `http://localhost:8000/docs`
   - Health check: `http://localhost:8000/health`
   - List models: `http://localhost:8000/models`

## Usage

### API Endpoints

- `POST /generate`: Generate text completions from your local LLM
- `GET /models`: List available models
- `GET /health`: Check service health status

### Integration Examples

```python
import requests

# Connect to your local LLM service
url = "http://localhost:8000/generate"
payload = {
    "prompt": "Explain quantum computing in simple terms",
    "max_tokens": 100
}
response = requests.post(url, json=payload)
print(response.json())
```

## Features

- **Local Hosting**: Run powerful language models entirely on your machine
- **Low Latency**: Direct access to models without internet roundtrip
- **Privacy**: Your data stays on your machine
- **Caching**: Redis caching layer for improved response times
- **Monitoring**: Track usage and performance with PostgreSQL
- **Multiple Models**: Support for various open-source LLMs
- **Resource Management**: Configure GPU/CPU usage and model loading

## Database

The project uses PostgreSQL to store usage metrics, performance data, and request history for monitoring and optimization.

## Caching

Redis is used for caching frequent responses and managing model states to reduce load times and improve response speed.

## Contributing

Feel free to submit issues or pull requests for improvements or bug fixes.

## License

This project is licensed under the MIT License.