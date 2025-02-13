from transformers import pipeline

class TextCorrector:
    def __init__(self, corrector):
        self.corrector = corrector

    def get_default_corrector():
        model_path = "model\sage-fredt5-large"
        return TextCorrector(corrector=pipeline("text2text-generation", model=model_path))
    
    def fix_spelling(self, text) -> str:
        return self.corrector(text)[0]['generated_text']