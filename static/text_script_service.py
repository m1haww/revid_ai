import requests
import time

class TextScriptService:
    def __init__(self, api_key):
        self.api_key = api_key

    def generate_video_script(self, prompt, max_retries=3, initial_delay=1):
        url = "https://api.openai.com/v1/responses"

        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.api_key}"
        }

        data = {
            "model": "ft:gpt-4o-mini-2024-07-18:personal:ai-copy-ad-maker:BedEIwVl",
            "input": prompt
        }

        for attempt in range(max_retries):
            try:
                response = requests.post(url, headers=headers, json=data)
                
                response_data = response.json()

                if response.status_code == 200:
                    return response_data["output"][0]["content"][0]["text"]
                else:
                    print(f"OpenAI API error (attempt {attempt + 1}/{max_retries}): {response_data}")
                    
                    if response.status_code >= 500 or (
                        isinstance(response_data, dict) and 
                        response_data.get('error', {}).get('type') == 'server_error'
                    ):
                        if attempt < max_retries - 1:
                            # Exponential backoff: 1s, 2s, 4s
                            delay = initial_delay * (2 ** attempt)
                            print(f"Retrying in {delay} seconds...")
                            time.sleep(delay)
                            continue
                    
                    return ""
            except Exception as e:
                print(f"Error calling OpenAI API (attempt {attempt + 1}/{max_retries}): {str(e)}")
                
                if attempt < max_retries - 1:
                    delay = initial_delay * (2 ** attempt)
                    print(f"Retrying in {delay} seconds...")
                    time.sleep(delay)
                    continue
                    
                return ""
        
        print(f"Failed to generate video script after {max_retries} attempts")
        return ""
