
curl -X POST "http://localhost:8000/generate" \
     -H "Content-Type: application/json" \
     -d '{
         "model_name": "qwen",
         "messages": [
             {
                 "role": "user",
                 "content": "What is machine learning, explain in one sentence?"
             }
         ],
         "max_tokens": 32768,
         "enable_thinking": false
     }'