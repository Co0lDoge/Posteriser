from template.poster_template import Template
from drawable.drawable_object import DrawableImage, DrawableText, TextAlignment, TextLine

DEFAULT_FONT = "arial.ttf"
DEFAULT_FONT_BOLD = "arialbd.ttf"
DEFAULT_FONT_SIZE = 50
DEFAULT_COLOR = (255, 255, 255)
DEFAULT_LINE_WIDTH = 4

def get_template_noman() -> Template:
    background_size = 1500
    return Template(
        background_size=background_size,
        logo=DrawableImage(
            size=(90, 90),
            position=(40, 80),
        ),
        logo_info=DrawableText(
            size=(1000, 120),
            position=(130, 70),
            font_path=DEFAULT_FONT,
            font_size=70,
            font_color=DEFAULT_COLOR,
            text_alignment=TextAlignment.LEFT
        ),
        event_title=DrawableText(
            size=(1400, 400),
            position=(int(background_size/2-1400/2), 200),
            font_path=DEFAULT_FONT_BOLD,
            font_size=100,
            font_color=DEFAULT_COLOR,
            text_alignment=TextAlignment.CENTER,
            text_line=TextLine.VERTICAL.set_line_width(DEFAULT_LINE_WIDTH)
        ),
        event_description=DrawableText(
            size=(1000, 800),
            position=(220, 500),
            font_path=DEFAULT_FONT,
            font_size=70,
            font_color=DEFAULT_COLOR,
            text_alignment=TextAlignment.CENTER
        ),
        event_time=DrawableText(
            size=(600, 200),
            position=(960, 10),
            font_path=DEFAULT_FONT_BOLD,
            font_size=65,
            font_color=DEFAULT_COLOR,
            text_alignment=TextAlignment.LEFT
        ),
        event_place=DrawableText(
            size=(500, 150),
            position=(960, 70),
            font_path=DEFAULT_FONT,
            font_size=DEFAULT_FONT_SIZE,
            font_color=DEFAULT_COLOR,
            text_alignment=TextAlignment.LEFT
        )
    )