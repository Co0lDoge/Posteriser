from PIL import Image
from argloader import load_args
from imagegen import ImageGenerator
from photo_transform import PhotoTransform
from text_transform import TextCorrector
from poster_merge import PosterGenerator

name, text = load_args()

poster_generator = PosterGenerator()

photo = Image.open('res/Professional-Headshot-Poses-Blog-Post-1.png')
background = ImageGenerator.generate_image_gradient()
backgroundless_photo = PhotoTransform.remove_background(photo)

text_corrector = TextCorrector.get_default_corrector()
corrected_text = text_corrector.fix_spelling(text)

poster = poster_generator.merge_content(background, backgroundless_photo, name, corrected_text)

# Show final poster
poster.show()
poster.save("output/poster.png")
