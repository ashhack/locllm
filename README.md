# LLM Pipeline Project

This project implements a pipeline for interacting with a local LLM model using FastAPI, Redis for caching, and PostgreSQL for storing chat history. The pipeline consists of two main agents: an Explainer agent and a Reasoning agent.

## Project Structure

```
llm-pipeline
├── src
│   ├── model_service
│   │   ├── __init__.py
│   │   ├── api.py
│   │   ├── config.py
│   │   └── ollama_client.py
│   ├── agents
│   │   ├── __init__.py
│   │   ├── explainer.py
│   │   └── reasoning.py
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

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd llm-pipeline
   ```

2. **Install dependencies**:
   Make sure you have Python 3.8 or higher installed. Then, install the required packages using pip:
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure the environment**:
   Update the `config/settings.py` file with your PostgreSQL and Redis configurations.

4. **Run the application**:
   Start the FastAPI server by running:
   ```bash
   uvicorn main:app --reload
   ```

5. **Access the API**:
   Open your browser and navigate to `http://localhost:8000/docs` to view the API documentation and test the endpoints.

## Usage

- Use the `/api` endpoint to interact with the LLM model.
- The Explainer agent can be used to get explanations for user queries.
- The Reasoning agent can provide logical conclusions based on the input.

## Database

The project uses PostgreSQL to store chat history. Ensure that your PostgreSQL server is running and accessible.

## Caching

Redis is used for caching checkpoints to improve performance. Make sure your Redis server is running.

## Contributing

Feel free to submit issues or pull requests for improvements or bug fixes.

## License

This project is licensed under the MIT License.