from drawable.drawable_object import DrawableImage, DrawableText, TextAlignment, TextLine
from dataclasses import dataclass

DEFAULT_FONT = "arial.ttf"
DEFAULT_FONT_BOLD = "arialbd.ttf"
DEFAULT_FONT_SIZE = 24
DEFAULT_COLOR = (255, 255, 255)

@dataclass
class Template:
    background_size: int
    speaker_photo: DrawableImage = None
    speaker_name: DrawableText = None
    speaker_name_info: DrawableText = None
    moderator_photo: DrawableImage = None
    moderator_name: DrawableText = None
    moderator_name_info: DrawableText = None
    logo: DrawableImage = None
    logo_info: DrawableText = None
    event_description: DrawableText = None
    event_title: DrawableText = None
    event_time: DrawableText = None
    event_place: DrawableText = None

def get_template_dualman() -> Template: 
    background_size = 900
    return Template(
        background_size=900,
        speaker_photo=DrawableImage(
            size=(None, 600),
            position=(-50, background_size - 600),
        ),
        speaker_name=DrawableText(
            size=(220, 100),
            position=(330, 540),
            font_path=DEFAULT_FONT,
            font_size=40,
            font_color=DEFAULT_COLOR,
            text_alignment=TextAlignment.LEFT,
            text_line=TextLine.LEFT
        ),
        speaker_name_info=DrawableText(
            size=(150, 100),
            position=(335, 620),
            font_path=DEFAULT_FONT,
            font_size=20,
            font_color=DEFAULT_COLOR,
            text_alignment=TextAlignment.LEFT
        ),
        moderator_photo=DrawableImage(
            size=(None, 600),
            position=(600, background_size - 600),
        ),
        moderator_name=DrawableText(
            size=(220, 100),
            position=(430, 690),
            font_path=DEFAULT_FONT,
            font_size=40,
            font_color=DEFAULT_COLOR,
            text_alignment=TextAlignment.LEFT,
            text_line=TextLine.LEFT
        ),
        moderator_name_info=DrawableText(
            size=(150, 100),
            position=(435, 770),
            font_path=DEFAULT_FONT,
            font_size=20,
            font_color=DEFAULT_COLOR,
            text_alignment=TextAlignment.LEFT
        ),
        logo=DrawableImage(
            size=(80, 80),
            position=(40, 30),
        ),
        logo_info=DrawableText(
            size=(500, 100),
            position=(110, 30),
            font_path=DEFAULT_FONT,
            font_size=40,
            font_color=DEFAULT_COLOR,
            text_alignment=TextAlignment.LEFT
        ),
        event_title=DrawableText(
            size=(800, 200),
            position=(int(background_size/2-800/2), 110),
            font_path=DEFAULT_FONT_BOLD,
            font_size=70,
            font_color=DEFAULT_COLOR,
            text_alignment=TextAlignment.CENTER,
            text_line=TextLine.VERTICAL
        ),
        event_description=DrawableText(
            size=(360, 200),
            position=(290, 310),
            font_path=DEFAULT_FONT,
            font_size=DEFAULT_FONT_SIZE,
            font_color=DEFAULT_COLOR,
            text_alignment=TextAlignment.CENTER
        ),
        event_time=DrawableText(
            size=(300, 70),
            position=(630, 10),
            font_path=DEFAULT_FONT_BOLD,
            font_size=30,
            font_color=DEFAULT_COLOR,
            text_alignment=TextAlignment.LEFT
        ),
        event_place=DrawableText(
            size=(200, 100),
            position=(630, 40),
            font_path=DEFAULT_FONT,
            font_size=DEFAULT_FONT_SIZE,
            font_color=DEFAULT_COLOR,
            text_alignment=TextAlignment.LEFT
        )
)

def get_template_singleman() -> Template:
    return Template(
        background_size=900
    )