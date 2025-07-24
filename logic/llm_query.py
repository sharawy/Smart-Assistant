import google.generativeai as genai
from config import GEMINI_API_KEY

class LLMQuery:
    def __init__(self, api_key=GEMINI_API_KEY):
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel('gemini-2.5-flash')

    def ask(self, prompt):
        try:
            response = self.model.generate_content(prompt)
            return response.text.strip()
        except Exception as e:
            return f"LLM Error: {e}" 