import requests

class RemotePipeline():
    def __init__(self, url):
        self.url = url

    def __call__(self, text):
        params = {"text": text}
        response = requests.get(f"{self.url}/correct", params=params)
        if response.status_code != 200:
            raise Exception(f"Error: {response.status_code}")
        return response.json()['result']

class TextCorrector:
    def __init__(self, corrector):
        self.corrector = corrector

    def get_default_corrector():
        from transformers import pipeline
        model_path = "model/sage-fredt5-large"
        return TextCorrector(corrector=pipeline("text2text-generation", model=model_path))
    
    def get_remote_corrector(url):
        remote_pipeline = RemotePipeline(url)
        return TextCorrector(corrector=remote_pipeline)
        
    def fix_spelling(self, text) -> str:
        return self.corrector(text)[0]['generated_text']