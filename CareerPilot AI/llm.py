import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

class LLMClient:
    def __init__(self):
        self.client = Groq(api_key=os.getenv("GROQ_API_KEY"))
        self.model = os.getenv("MODEL_NAME","llama-3.3-70b-versatile")
    
    def generate(self, prompt: str, max_tokens: int = 2000, temperature: float = 0.7) -> str:
        """Generate text using Groq AI"""
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": "You are an expert career guidance AI assistant. Provide detailed, actionable advice."},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=max_tokens,
                temperature=temperature
            )
            return response.choices[0].message.content
        except Exception as e:
            print(f"Error generating response: {e}")
            return "Unable to generate response at this time."
    
    def generate_structured(self, prompt: str, format_instruction: str = "") -> str:
        """Generate structured response"""
        full_prompt = f"{prompt}\n\n{format_instruction}" if format_instruction else prompt
        return self.generate(full_prompt)