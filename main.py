from PIL import Image
from argloader import argloader
from imagegen import generate_image_gradient
from photo_transform import remove_background, resize
from text_transform import fix_spelling
from poster_merge import merge_content

photo = Image.open('res/Professional-Headshot-Poses-Blog-Post-1.png')
background = generate_image_gradient()

name = argloader()[0]
text = argloader()[1]

corrected_text = str(fix_spelling(text))

backgroundless_photo = resize(remove_background(photo))
resized_photo = resize(backgroundless_photo, width=400)
poster = merge_content(background, resized_photo, name, corrected_text)

# Show final poster
poster.show()
poster.save("output/poster.png")
