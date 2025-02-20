from template.poster_template import Template
from drawable.drawable_object import DrawableImage, DrawableText, TextAlignment, TextLine

DEFAULT_FONT = "arial.ttf"
DEFAULT_FONT_BOLD = "arialbd.ttf"
DEFAULT_FONT_SIZE = 40
DEFAULT_COLOR = (255, 255, 255)
DEFAULT_LINE_WIDTH = 4

def get_template_singleman() -> Template:
    background_size = 1500
    return Template(
        background_size=background_size,
        speaker_photo=DrawableImage(
            size=(None, 900),
            position=(140, background_size-900),
        ),
        speaker_name=DrawableText(
            size=(550, 200),
            position=(930, 940),
            font_path=DEFAULT_FONT_BOLD,
            font_size=80,
            font_color=DEFAULT_COLOR,
            text_alignment=TextAlignment.LEFT,
            text_line=TextLine.LEFT.set_line_width(DEFAULT_LINE_WIDTH)
        ),
        speaker_info=DrawableText(
            size=(450, 200),
            position=(935, 1100),
            font_path=DEFAULT_FONT,
            font_size=60,
            font_color=DEFAULT_COLOR,
            text_alignment=TextAlignment.LEFT
        ),
    )