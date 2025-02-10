from PIL import Image
from argloader import argloader
from imagegen import generate_image
from photo_transform import remove_background

photo = Image.open('res/Professional-Headshot-Poses-Blog-Post-1.png')
background = generate_image()
name = argloader()[0]

backgroundless_photo = remove_background(photo)
backgroundless_photo.show()


