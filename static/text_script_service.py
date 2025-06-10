import requests

class TextScriptService:
    def __init__(self, api_key):
        self.api_key = api_key

    def generate_video_script(self, prompt):
        url = "https://api.openai.com/v1/responses"

        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.api_key}"
        }

        data = {
            "model": "ft:gpt-4o-mini-2024-07-18:personal:ai-copy-ad-maker:BedEIwVl",
            "input": prompt
        }

        try:
            response = requests.post(url, headers=headers, json=data)
            
            response_data = response.json()

            if response.status_code == 200:
                return response_data["output"][0]["content"][0]["text"]
            else:
                print(f"OpenAI API error: {response_data}")
                return ""
        except Exception as e:
            print(f"Error calling OpenAI API: {str(e)}")
            return ""
