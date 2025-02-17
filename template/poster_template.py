from drawable.drawable_object import DrawableImage, DrawableText
from dataclasses import dataclass

DEFAULT_FONT = "arial.ttf"
DEFAULT_FONT_SIZE = 24
DEFAULT_COLOR = (255, 255, 255)

@dataclass
class Template:
    background_size: int
    photo: DrawableImage
    description: DrawableText
    name: DrawableText
    title: DrawableText

def get_default_template() -> Template: 
    background_size = 900
    return Template(
        background_size=900,
        photo=DrawableImage(
            size=(None, 600),
            position=(-50, background_size - 600),
        ),
        description=DrawableText(
            size=(400, 200),
            position=(300, 200),
            font_path=DEFAULT_FONT,
            font_size=DEFAULT_FONT_SIZE,
            font_color=DEFAULT_COLOR,
        ),
        name=DrawableText(
            size=(220, 100),
            position=(330, 570),
            font_path=DEFAULT_FONT,
            font_size=40,
            font_color=DEFAULT_COLOR,
        ),
        title=DrawableText(
            size=(500, 200),
            position=(int(background_size/2-500/2), 100),
            font_path=DEFAULT_FONT,
            font_size=50,
            font_color=DEFAULT_COLOR
        )
)