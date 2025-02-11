# model pipeline
from transformers import pipeline

corrector = pipeline("text2text-generation", model="ai-forever/sage-fredt5-large")

def fix_spelling(text):
    return corrector(text)[0]['generated_text']