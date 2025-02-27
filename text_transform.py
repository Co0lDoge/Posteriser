from transformers import pipeline
import requests

class RemoteCorrector():
    def __init__(self, url):
        self.url = url

    def fix_spelling(self, text) -> str:
        response = requests.get(f"{self.url}/correct/{text}")
        return response.json()['result']
    
    def __call__(self, text):
        return self.fix_spelling(text)

class TextCorrector:
    def __init__(self, corrector):
        self.corrector = corrector

    def get_default_corrector():
        model_path = "model\sage-fredt5-large"
        return TextCorrector(corrector=pipeline("text2text-generation", model=model_path))
    
    def get_remote_corrector(url):
        remote_corrector = RemoteCorrector(url)
        return TextCorrector(corrector=remote_corrector)
        
    def fix_spelling(self, text) -> str:
        return self.corrector(text)[0]['generated_text']