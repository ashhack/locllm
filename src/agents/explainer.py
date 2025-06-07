class ExplainerAgent:
    def __init__(self, model_client):
        self.model_client = model_client

    def explain(self, query: str) -> str:
        """Process the user query and provide an explanation."""
        response = self.model_client.send_request(query)
        explanation = self._process_response(response)
        return explanation

    def _process_response(self, response) -> str:
        """Extract and format the explanation from the model's response."""
        # Assuming the response contains an 'explanation' field
        return response.get('explanation', 'No explanation available.')