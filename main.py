from PIL import Image
from argloader import load_args
from imagegen import ImageGenerator
from photo_transform import PhotoTransform
from text_transform import TextCorrector
from poster_merge import PosterBuilder
from template.poster_template import get_template_dualman

POSTER_DEBUG = False

(
    speaker_name,
    speaker_name_info,
    speaker_photo,
    moderator_name,
    moderator_name_info,
    moderator_photo,
    logo,
    logo_info,
    event_desc,
    event_title,
    event_time,
    event_place
) = load_args()

poster_template = get_template_dualman()

background = ImageGenerator.generate_image_gradient(
    width=poster_template.background_size, 
    height=poster_template.background_size
)

speaker_photo = Image.open(speaker_photo)
speaker_backgroundless_photo = PhotoTransform.remove_background(speaker_photo)
moderator_photo = Image.open(moderator_photo)
moderator_backgroundless_photo = PhotoTransform.remove_background(moderator_photo)
logo = Image.open(logo).convert("RGBA")
backgroundless_logo = PhotoTransform.remove_background(logo)

text_corrector = TextCorrector.get_default_corrector()
corrected_text = text_corrector.fix_spelling(event_desc)

poster_builder = PosterBuilder(POSTER_DEBUG)
poster = (
        poster_builder
        .set_template(poster_template)
        .set_background(background)
        .set_speaker_photo(speaker_backgroundless_photo)
        .set_speaker_name(speaker_name)
        .set_speaker_name_info(speaker_name_info)
        .set_moderator_photo(moderator_backgroundless_photo)
        .set_moderator_name(moderator_name)
        .set_moderator_name_info(moderator_name_info)
        .set_logo(backgroundless_logo)
        .set_logo_info(logo_info)
        .set_event_description(corrected_text)
        .set_event_title(event_title)
        .set_event_time(event_time)
        .set_event_place(event_place)
        .build()
    )

# Show final poster
poster.show()
poster.save("output/poster.png")
