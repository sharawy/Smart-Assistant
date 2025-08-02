import google.generativeai as genai
from config import GEMINI_API_KEY

# Wrapper for querying the Gemini LLM model using the Generative AI API
class LLMQuery:

    # Initialize and configure Gemini model with provided API key
    def __init__(self, api_key=GEMINI_API_KEY):
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel('gemini-2.5-flash')

    # Send prompt to the LLM and return the generated response text
    def ask(self, prompt):
        try:
            response = self.model.generate_content(prompt)
            return response.text.strip()
        except Exception as e:
            return f"LLM Error: {e}" 