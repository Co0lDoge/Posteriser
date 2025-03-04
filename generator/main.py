from PIL import Image
from argloader import load_args
from imagegen import ImageGenerator
from background_remover import BackgroundRemover
from text_transform import TextCorrector
from poster.poster_builder import PosterBuilder
from template.template_selector import select_template

# Done: Color selection
# Done: Company name extension
# Done: Color scheme
# TODO: Config that selects corrector
# TODO: Cards for names (white radial corners with black text)
# TODO: Move rembg to server for clearing logos

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
    event_place,
    color_scheme,
    output_path
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
    logo_info,
    event_place,
)

background = ImageGenerator.generate_image_gradient(
    width=poster_template.background_size, 
    height=poster_template.background_size,
    start_color=color_scheme,
)
overlay = ImageGenerator.generate_transparent_gradient(
    width=poster_template.background_size, 
    height=poster_template.background_size,
    start_color=color_scheme,
    end_color=(color_scheme[0]/2.55, color_scheme[1]/2.55, color_scheme[2]/2.55),
)

background_remover = BackgroundRemover.get_remote_pipeline(url="http://localhost:8000")
local_background_remover = BackgroundRemover.get_remote_pipeline(url="http://localhost:8000") # Dont work with non u2net models
if speaker_photo:
    speaker_photo = Image.open(speaker_photo)
    speaker_photo = background_remover.remove_background(speaker_photo).convert('RGBA')
if moderator_photo:
    moderator_photo = Image.open(moderator_photo)
    moderator_photo = background_remover.remove_background(moderator_photo).convert('RGBA')
if presenter_photo:
    presenter_photo = Image.open(presenter_photo)
    presenter_photo = background_remover.remove_background(presenter_photo).convert('RGBA')
if logo:
    logo = Image.open(logo)
    backgroundless_logo = local_background_remover.remove_background(logo).convert('RGBA')

text_corrector = TextCorrector.get_remote_corrector(url="http://localhost:8000")
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
#poster.show()
poster.save(output_path)
