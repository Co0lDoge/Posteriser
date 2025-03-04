from template.poster_template import Template
from drawable.drawable_object import DrawableImage, DrawableText, TextAlignment, TextLine

DEFAULT_FONT = "arial.ttf"
DEFAULT_FONT_BOLD = "arialbd.ttf"
DEFAULT_FONT_SIZE = 50
DEFAULT_COLOR = (255, 255, 255)
DEFAULT_LINE_WIDTH = 4

def get_template_dualman() -> Template:
    background_size = 1500
    return Template(
        background_size=background_size,
        speaker_photo=DrawableImage(
            size=(None, 900),
            position=(-50, background_size-900),
            overlay=True
        ),
        speaker_name=DrawableText(
            size=(350, 400),
            position=(730, 940),
            font_path=DEFAULT_FONT_BOLD,
            font_size=60,
            font_color=DEFAULT_COLOR,
            text_alignment=TextAlignment.LEFT,
            text_line=TextLine.LEFT.set_line_width(DEFAULT_LINE_WIDTH)
        ),
        speaker_info=DrawableText(
            size=(350, 400),
            position=(500, 900),
            font_path=DEFAULT_FONT,
            font_size=45,
            font_color=DEFAULT_COLOR,
            text_alignment=TextAlignment.LEFT,
            text_line=TextLine.LEFT.set_line_width(DEFAULT_LINE_WIDTH)
        ),
        moderator_photo=DrawableImage(
            size=(None, 900),
            position=(950, background_size-900),
            overlay=False
        ),
        moderator_name=DrawableText(
            size=(350, 400),
            position=(50, 600),
            font_path=DEFAULT_FONT_BOLD,
            font_size=60,
            font_color=DEFAULT_COLOR,
            text_alignment=TextAlignment.LEFT,
            text_line=TextLine.LEFT.set_line_width(DEFAULT_LINE_WIDTH)
        ),
        moderator_info=DrawableText(
            size=(350, 400),
            position=(800, 1150),
            font_path=DEFAULT_FONT,
            font_size=45,
            font_color=DEFAULT_COLOR,
            text_alignment=TextAlignment.LEFT,
            text_line=TextLine.LEFT.set_line_width(DEFAULT_LINE_WIDTH)
        ),
        logo=DrawableImage(
            size=(90, 90),
            position=(40, 80),
        ),
        logo_info=DrawableText(
            size=(1200, 120),
            position=(130, 80),
            font_path=DEFAULT_FONT,
            font_size=50,
            font_color=DEFAULT_COLOR,
            text_alignment=TextAlignment.LEFT
        ),
        event_title=DrawableText(
            size=(1400, 250),
            position=(int(background_size/2-1400/2), 200),
            font_path=DEFAULT_FONT_BOLD,
            font_size=80,
            font_color=DEFAULT_COLOR,
            text_alignment=TextAlignment.CENTER,
            text_line=TextLine.VERTICAL.set_line_width(DEFAULT_LINE_WIDTH)
        ),
        event_description=DrawableText(
            size=(1400, 190),
            position=(50, 400),
            font_path=DEFAULT_FONT,
            font_size=DEFAULT_FONT_SIZE-10,
            font_color=DEFAULT_COLOR,
            text_alignment=TextAlignment.CENTER
        ),
        event_time=DrawableText(
            size=(500, 200),
            position=(500, 580),
            font_path=DEFAULT_FONT_BOLD,
            font_size=65,
            font_color=DEFAULT_COLOR,
            text_alignment=TextAlignment.CENTER,
            text_line=TextLine.VERTICAL.set_line_width(DEFAULT_LINE_WIDTH)
        ),
        event_place=DrawableText(
            size=(500, 400),
            position=(150, 70),
            font_path=DEFAULT_FONT,
            font_size=DEFAULT_FONT_SIZE,
            font_color=DEFAULT_COLOR,
            text_alignment=TextAlignment.CENTER,
            text_line=TextLine.VERTICAL.set_line_width(DEFAULT_LINE_WIDTH)
        ),
        groups = {
            "speaker": ["speaker_info", "speaker_name"],
            "moderator": ["moderator_info", "moderator_name"],
            "time_place": ["event_time", "event_place"],
        }
    )