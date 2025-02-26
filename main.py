from PIL import Image
from argloader import load_args
from imagegen import ImageGenerator
from background_remover import BackgroundRemover
from text_transform import TextCorrector
from poster.poster_builder import PosterBuilder
from template.template_selector import select_template

# TODO: Color selection
# TODO: Company name extension

POSTER_DEBUG = False

(
    speaker_name,
    speaker_info,
    speaker_photo,
    moderator_name,
    moderator_info,
    moderator_photo,
    presenter_name,
    presenter_info,
    presenter_photo,
    logo,
    logo_info,
    event_desc,
    event_title,
    event_time,
    event_place
) = load_args()

poster_template = select_template(
    speaker_name,
    speaker_info,
    speaker_photo,
    moderator_name,
    moderator_info,
    moderator_photo,
    presenter_name,
    presenter_info,
    presenter_photo,
)

background = ImageGenerator.generate_image_gradient(
    width=poster_template.background_size, 
    height=poster_template.background_size
)
overlay = ImageGenerator.generate_transparent_gradient(
    width=poster_template.background_size, 
    height=poster_template.background_size
)
if speaker_photo:
    speaker_photo = Image.open(speaker_photo)
    speaker_photo = BackgroundRemover.remove_background(speaker_photo)
if moderator_photo:
    moderator_photo = Image.open(moderator_photo)
    moderator_photo = BackgroundRemover.remove_background(moderator_photo)
if presenter_photo:
    presenter_photo = Image.open(presenter_photo)
    presenter_photo = BackgroundRemover.remove_background(presenter_photo)
if logo:
    logo = Image.open(logo).convert("RGBA")
    backgroundless_logo = BackgroundRemover.remove_background(logo)

text_corrector = TextCorrector.get_default_corrector()
corrected_text = text_corrector.fix_spelling(event_desc)

poster_builder = PosterBuilder(POSTER_DEBUG)
poster = (
        poster_builder
        .set_template(poster_template)
        .set_background(background)
        .set_overlay(overlay)
        .set_speaker_photo(speaker_photo)
        .set_speaker_name(speaker_name)
        .set_speaker_info(speaker_info)
        .set_moderator_photo(moderator_photo)
        .set_moderator_name(moderator_name)
        .set_moderator_info(moderator_info)
        .set_presenter_photo(presenter_photo)
        .set_presenter_name(presenter_name)
        .set_presenter_info(presenter_info)
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
