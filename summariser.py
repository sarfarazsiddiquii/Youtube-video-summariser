import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

class GeminiSummariser:
    def __init__(self):
        api_key = os.getenv('API_KEY')
        if not api_key:
            raise ValueError("API key is not provided")
        
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel('gemini-pro')

    def summarize_transcript(self, transcript: str) -> str:
        try:
            prompt = f"""
            Please provide a detailed summary of these videos in detail.
            
            Transcript:
            {transcript}
            """
            
            response = self.model.generate_content(prompt)
            return response.text
        
        except Exception as e:
            print(f"Error in summarization: {str(e)}")
            return f"Failed to generate summary: {str(e)}"

