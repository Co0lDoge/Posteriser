from template.poster_template import Template
from drawable.drawable_object import DrawableImage, DrawableText, TextAlignment, TextLine, TextBackground

DEFAULT_FONT = "arial.ttf"
DEFAULT_FONT_BOLD = "arialbd.ttf"
DEFAULT_FONT_SIZE = 50
DEFAULT_COLOR = (255, 255, 255)
DEFAULT_LINE_WIDTH = 4

def get_template_singleman() -> Template:
    background_size = 1500
    return Template(
        background_size=background_size,
        speaker_photo=DrawableImage(
            size=(None, 1000),
            position=(800, background_size-1000),
            overlay=True
        ),
        speaker_name=DrawableText(
            size=(550, 200),
            position=(70, 940),
            font_path=DEFAULT_FONT_BOLD,
            font_size=60,
            font_color=DEFAULT_COLOR,
            text_alignment=TextAlignment.LEFT,
            text_background=TextBackground.ROUNDED
        ),
        speaker_info=DrawableText(
            size=(450, 200),
            position=(735, 1100),
            font_path=DEFAULT_FONT,
            font_size=50,
            font_color=DEFAULT_COLOR,
            text_alignment=TextAlignment.LEFT,
            text_background=TextBackground.ROUNDED
        ),
        moderator_photo=DrawableImage(
            size=(None, 1000),
            position=(800, background_size-1000),
            overlay=True
        ),
        moderator_name=DrawableText(
            size=(550, 200),
            position=(70, 940),
            font_path=DEFAULT_FONT_BOLD,
            font_size=60,
            font_color=DEFAULT_COLOR,
            text_alignment=TextAlignment.LEFT,
            text_background=TextBackground.ROUNDED
        ),
        moderator_info=DrawableText(
            size=(450, 200),
            position=(735, 1100),
            font_path=DEFAULT_FONT,
            font_size=50,
            font_color=DEFAULT_COLOR,
            text_alignment=TextAlignment.LEFT,
            text_line=TextLine.LEFT.set_line_width(DEFAULT_LINE_WIDTH)
        ),
        logo=DrawableImage(
            size=(180, 180),
            position=(80, 1300),
            overlay=True
        ),
        logo_info=DrawableText(
            size=(800, 350),
            position=(700, 50),
            font_path=DEFAULT_FONT,
            font_size=50,
            font_color=DEFAULT_COLOR,
            text_alignment=TextAlignment.LEFT,
            text_line=TextLine.LEFT.set_line_width(DEFAULT_LINE_WIDTH)
        ),
        event_title=DrawableText(
            size=(1400, 250),
            position=(int(background_size/2-1400/2), 300),
            font_path=DEFAULT_FONT_BOLD,
            font_size=80,
            font_color=DEFAULT_COLOR,
            text_alignment=TextAlignment.CENTER,
            text_line=TextLine.VERTICAL.set_line_width(DEFAULT_LINE_WIDTH)
        ),
        event_description=DrawableText(
            size=(750, 500),
            position=(70, 440),
            font_path=DEFAULT_FONT,
            font_size=DEFAULT_FONT_SIZE,
            font_color=DEFAULT_COLOR,
            text_alignment=TextAlignment.LEFT,
            text_line=TextLine.LEFT.set_line_width(DEFAULT_LINE_WIDTH)
        ),
        event_time=DrawableText(
            size=(600, 200),
            position=(50, 70),
            font_path=DEFAULT_FONT_BOLD,
            font_size=65,
            font_color=DEFAULT_COLOR,
            text_alignment=TextAlignment.LEFT
        ),
        event_place=DrawableText(
            size=(650, 350),
            position=(50, 70),
            font_path=DEFAULT_FONT,
            font_size=DEFAULT_FONT_SIZE,
            font_color=DEFAULT_COLOR,
            text_alignment=TextAlignment.LEFT
        ),
        groups = {
            "speaker": ["speaker_name", "speaker_info"],
            "moderator": ["moderator_name", "moderator_info"],
            "time_place": ["event_time", "event_place"],
        }
    )