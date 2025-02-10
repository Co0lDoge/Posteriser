from autocorrect import Speller

# Initialize the spell checker for Russian
spell = Speller(lang='ru')

# Sample text with a misspelled word
text = "Пример с ашибкой в слове."

# Correct the text
corrected_text = spell(text)
print(corrected_text)  # "Пример с ошибкой в слове."