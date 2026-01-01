import requests
import json

class OllamaClient:
    """
    Reusable LLM client for Ollama API.
    Wraps all API calls in one place.
    """
    
    def __init__(self, model="llama3.2", base_url="http://localhost:11434"):
        self.model = model
        self.base_url = base_url
        self.api_url = f"{base_url}/api/generate"
    
    def generate(self, prompt, max_tokens=500):
        """Generate text from prompt"""
        try:
            payload = {
                "model": self.model,
                "prompt": prompt,
                "stream": False,
                "options": {
                    "temperature": 0.7,
                    "num_predict": max_tokens
                }
            }
            
            response = requests.post(
                self.api_url,
                json=payload,
                timeout=60
            )
            
            if response.status_code == 200:
                return response.json()['response']
            else:
                print(f"Error: Ollama API returned {response.status_code}")
                return ""
                
        except requests.exceptions.ConnectionError:
            print("Error: Cannot connect to Ollama. Make sure Ollama is running.")
            print("Run: ollama serve")
            return ""
        except Exception as e:
            print(f"Error generating text: {e}")
            return ""