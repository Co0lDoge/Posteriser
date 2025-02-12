from PIL import Image
from argloader import load_args
from imagegen import ImageGenerator
from photo_transform import PhotoTransform
from text_transform import TextCorrector
from poster_merge import PosterBuilder
from poster_template import Template

name, text = load_args()

photo = Image.open('res/Professional-Headshot-Poses-Blog-Post-1.png')
background = ImageGenerator.generate_image_gradient()
backgroundless_photo = PhotoTransform.remove_background(photo)

text_corrector = TextCorrector.get_default_corrector()
corrected_text = text_corrector.fix_spelling(text)

poster_builder = PosterBuilder()
poster = (
        poster_builder
        .set_template(Template.get_default_template())
        .set_background(background)
        .set_photo(backgroundless_photo)
        .set_desc("Welcome to the Event!")
        .build()
    )

# Show final poster
poster.show()
poster.save("output/poster.png")
