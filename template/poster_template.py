from drawable.drawable_object import DrawableImage, DrawableText, TextAlignment, TextLine
from dataclasses import dataclass

DEFAULT_FONT = "arial.ttf"
DEFAULT_FONT_BOLD = "arialbd.ttf"
DEFAULT_FONT_SIZE = 24
DEFAULT_COLOR = (255, 255, 255)

@dataclass
class Template:
    background_size: int
    photo: DrawableImage
    logo: DrawableImage
    logo_info: DrawableText
    description: DrawableText
    name: DrawableText
    name_info: DrawableText
    title: DrawableText

def get_default_template() -> Template: 
    background_size = 900
    return Template(
        background_size=900,
        photo=DrawableImage(
            size=(None, 600),
            position=(-50, background_size - 600),
        ),
        logo=DrawableImage(
            size=(110, 110),
            position=(30, 30),
        ),
        logo_info=DrawableText(
            size=(600, 100),
            position=(110, 20),
            font_path=DEFAULT_FONT,
            font_size=40,
            font_color=DEFAULT_COLOR,
            text_alignment=TextAlignment.LEFT
        ),
        description=DrawableText(
            size=(400, 200),
            position=(270, 250),
            font_path=DEFAULT_FONT,
            font_size=DEFAULT_FONT_SIZE,
            font_color=DEFAULT_COLOR,
            text_alignment=TextAlignment.CENTER
        ),
        name=DrawableText(
            size=(220, 100),
            position=(330, 540),
            font_path=DEFAULT_FONT,
            font_size=40,
            font_color=DEFAULT_COLOR,
            text_alignment=TextAlignment.LEFT,
            text_line=TextLine.LEFT
        ),
        name_info=DrawableText(
            size=(150, 100),
            position=(335, 600),
            font_path=DEFAULT_FONT,
            font_size=20,
            font_color=DEFAULT_COLOR,
            text_alignment=TextAlignment.LEFT
        ),
        title=DrawableText(
            size=(800, 200),
            position=(int(background_size/2-800/2), 100),
            font_path=DEFAULT_FONT_BOLD,
            font_size=70,
            font_color=DEFAULT_COLOR,
            text_alignment=TextAlignment.CENTER,
            text_line=TextLine.VERTICAL
        )
)