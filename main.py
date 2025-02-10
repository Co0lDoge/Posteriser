from PIL import Image, ImageDraw, ImageFont
from autocorrect import Speller
from argloader import argloader
from imagegen import generate_image_gradient
from photo_transform import remove_background, resize
from poster_merge import merge_content

photo = Image.open('res/Professional-Headshot-Poses-Blog-Post-1.png')
background = generate_image_gradient()
name = argloader()[0]
text = argloader()[1]

# Корректировка текста
spell = Speller(lang='ru')
text = "Пример с ашибкой в слове."
corrected_text = spell(text)

# Чистка фона фотографии и изменение размера
backgroundless_photo = resize(remove_background(photo))
resized_photo = resize(backgroundless_photo, width=400)

poster = merge_content(background, resized_photo, name, corrected_text)
poster.show()

