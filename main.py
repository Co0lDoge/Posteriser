from PIL import Image
from argloader import load_args
from imagegen import ImageGenerator
from photo_transform import PhotoTransform
from text_transform import TextCorrector
from poster_merge import PosterBuilder
from template.poster_template import get_default_template

name, desc, title = load_args()
poster_template = get_default_template()

background = ImageGenerator.generate_image_gradient(
    width=poster_template.background_size, 
    height=poster_template.background_size
)

photo = Image.open('res/Professional-Headshot-Poses-Blog-Post-1.png')
backgroundless_photo = PhotoTransform.remove_background(photo)
logo = Image.open('res/logo_alt.png').convert("RGBA")
backgroundless_logo = PhotoTransform.remove_background(logo)

text_corrector = TextCorrector.get_default_corrector()
corrected_text = text_corrector.fix_spelling(desc)

poster_builder = PosterBuilder()
poster = (
        poster_builder
        .set_template(poster_template)
        .set_background(background)
        .set_photo(backgroundless_photo)
        .set_logo(backgroundless_logo)
        .set_description(corrected_text)
        .set_name(name)
        .set_title(title)
        .build()
    )

# Show final poster
poster.show()
poster.save("output/poster.png")
