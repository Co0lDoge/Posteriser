from PIL import Image
from argloader import load_args
from imagegen import ImageGenerator
from photo_transform import PhotoTransform
from text_transform import TextTransform
from poster_merge import PosterGenerator

imagegen = ImageGenerator()
photo_transform = PhotoTransform()
text_transform = TextTransform()
poster_generator = PosterGenerator()

photo = Image.open('res/Professional-Headshot-Poses-Blog-Post-1.png')
background = imagegen.generate_image_gradient()

name, text = load_args()

corrected_text = text_transform.fix_spelling(text)

backgroundless_photo = photo_transform.remove_background(photo)
poster = poster_generator.merge_content(background, backgroundless_photo, name, corrected_text)

# Show final poster
poster.show()
poster.save("output/poster.png")
