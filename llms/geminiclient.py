import os
import google.generativeai as genai
from llms.basellm import BaseLLM

class GeminiClient(BaseLLM):
    def __init__(self, model: str = "gemini-1.5-flash"):
        
        api_key = os.environ.get("GEMINI_API_KEY")
        
        if not api_key:
            raise ValueError("GEMINI_API_KEY environment variable is missing!")
            
        # Configure Google's SDK
        genai.configure(api_key=api_key)
        
        # Initialize the model
        self.model = genai.GenerativeModel(model)
    
    def generate(self, system_prompt: str, user_prompt: str) -> str:
        try:
            full_prompt = f"System Instructions:\n{system_prompt}\n\nUser Input:\n{user_prompt}"
            
            response = self.model.generate_content(full_prompt)
            return response.text
            
        except Exception as e:
            return f"Error: Gemini API failed with message: {str(e)}"