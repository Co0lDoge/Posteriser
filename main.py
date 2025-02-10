from PIL import Image
from argloader import argloader
from imagegen import generate_image_gradient
from photo_transform import remove_background, resize

photo = Image.open('res/Professional-Headshot-Poses-Blog-Post-1.png')
background = generate_image_gradient()
name = argloader()[0]

backgroundless_photo = resize(remove_background(photo))
resized_photo = resize(backgroundless_photo, width=400)

position = (0, 900 - 400)
background.paste(resized_photo, position)
background.show()


