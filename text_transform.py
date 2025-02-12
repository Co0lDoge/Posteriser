from transformers import pipeline

class TextCorrector:
    def __init__(self, corrector):
        self.corrector = corrector

    def get_default_corrector():
        return TextCorrector(corrector=pipeline("text2text-generation", model="ai-forever/sage-fredt5-large"))
    
    def fix_spelling(self, text) -> str:
        return self.corrector(text)[0]['generated_text']