from transformers import pipeline

class TextTransform:
    def __init__(self):
        self.corrector = pipeline("text2text-generation", model="ai-forever/sage-fredt5-large")
    
    def fix_spelling(self, text):
        return self.corrector(text)[0]['generated_text']