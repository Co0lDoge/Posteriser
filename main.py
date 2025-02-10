import time
from PIL import Image, ImageDraw, ImageFont
from autocorrect import Speller
from argloader import argloader
from imagegen import generate_image_gradient
from photo_transform import remove_background, resize
from poster_merge import merge_content

# Timer start for photo loading and background generation
start_time = time.time()

photo = Image.open('res/Professional-Headshot-Poses-Blog-Post-1.png')
background = generate_image_gradient()

end_time = time.time()
print(f"Time for photo loading and background generation: {end_time - start_time:.4f} seconds")

# Timer start for text correction
start_time = time.time()

name = argloader()[0]
text = argloader()[1]

# Корректировка текста
spell = Speller(lang='ru')
text = "Пример с ашибкой в слове."
corrected_text = spell(text)

end_time = time.time()
print(f"Time for text correction: {end_time - start_time:.4f} seconds")

# Timer start for background removal and resizing
start_time = time.time()

backgroundless_photo = resize(remove_background(photo))
resized_photo = resize(backgroundless_photo, width=400)

end_time = time.time()
print(f"Time for background removal and resizing: {end_time - start_time:.4f} seconds")

# Timer start for content merging and final output
start_time = time.time()

poster = merge_content(background, resized_photo, name, corrected_text)

end_time = time.time()
print(f"Time for content merging and final output: {end_time - start_time:.4f} seconds")

# Show final poster
poster.show()
