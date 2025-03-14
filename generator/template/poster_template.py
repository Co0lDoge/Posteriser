from drawable.drawable_object import DrawableImage, DrawableText
from dataclasses import dataclass

@dataclass
class Template:
    background_size: int
    speaker_photo: DrawableImage = None
    speaker_name: DrawableText = None
    speaker_info: DrawableText = None
    moderator_photo: DrawableImage = None
    moderator_name: DrawableText = None
    moderator_info: DrawableText = None
    presenter_photo: DrawableImage = None
    presenter_name: DrawableText = None
    presenter_info: DrawableText = None
    logo: DrawableImage = None
    logo_info: DrawableText = None
    event_description: DrawableText = None
    event_title: DrawableText = None
    event_time: DrawableText = None
    event_place: DrawableText = None
    groups: dict[list[DrawableText]] = None