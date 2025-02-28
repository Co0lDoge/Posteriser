from template.poster_template import Template
from drawable.drawable_object import DrawableImage, DrawableText, TextAlignment, TextLine, TextBackground

DEFAULT_FONT = "arial.ttf"
DEFAULT_FONT_BOLD = "arialbd.ttf"
DEFAULT_FONT_SIZE = 50
DEFAULT_COLOR = (255, 255, 255)
DEFAULT_LINE_WIDTH = 4
DEFAULT_TEXT_BACKGROUND_COLOR = (0, 0, 255)

def get_template_threeman() -> Template:
    background_size = 1500
    return Template(
        background_size=background_size,
        speaker_photo=DrawableImage(
            size=(None, 800),
            position=(-50, background_size-800),
            overlay=True
        ),
        speaker_name=DrawableText(
            size=(250, 400),
            position=(730, 940),
            font_path=DEFAULT_FONT_BOLD,
            font_size=45,
            font_color=DEFAULT_COLOR,
            text_alignment=TextAlignment.LEFT,
            text_line=TextLine.LEFT.set_line_width(DEFAULT_LINE_WIDTH),
            text_background=TextBackground.ROUNDED.set_color(DEFAULT_TEXT_BACKGROUND_COLOR)
        ),
        speaker_info=DrawableText(
            size=(250, 400),
            position=(230, 1200),
            font_path=DEFAULT_FONT,
            font_size=30,
            font_color=DEFAULT_COLOR,
            text_alignment=TextAlignment.LEFT,
            text_line=TextLine.LEFT.set_line_width(DEFAULT_LINE_WIDTH),
            text_background=TextBackground.ROUNDED.set_color(DEFAULT_TEXT_BACKGROUND_COLOR)
        ),
        moderator_photo=DrawableImage(
            size=(None, 800),
            position=(450, background_size-800),
            overlay=True
        ),
        moderator_name=DrawableText(
            size=(250, 400),
            position=(50, 600),
            font_path=DEFAULT_FONT_BOLD,
            font_size=45,
            font_color=DEFAULT_COLOR,
            text_alignment=TextAlignment.LEFT,
            text_line=TextLine.LEFT.set_line_width(DEFAULT_LINE_WIDTH),
            text_background=TextBackground.ROUNDED.set_color(DEFAULT_TEXT_BACKGROUND_COLOR)
        ),
        moderator_info=DrawableText(
            size=(250, 400),
            position=(700, 1200),
            font_path=DEFAULT_FONT,
            font_size=30,
            font_color=DEFAULT_COLOR,
            text_alignment=TextAlignment.LEFT,
            text_line=TextLine.LEFT.set_line_width(DEFAULT_LINE_WIDTH),
            text_background=TextBackground.ROUNDED.set_color(DEFAULT_TEXT_BACKGROUND_COLOR)
        ),
        presenter_photo=DrawableImage(
            size=(None, 800),
            position=(900, background_size-800),
            overlay=True
        ),
        presenter_name=DrawableText(
            size=(250, 400),
            position=(730, 940),
            font_path=DEFAULT_FONT_BOLD,
            font_size=45,
            font_color=DEFAULT_COLOR,
            text_alignment=TextAlignment.LEFT,
            text_line=TextLine.LEFT.set_line_width(DEFAULT_LINE_WIDTH),
            text_background=TextBackground.ROUNDED.set_color(DEFAULT_TEXT_BACKGROUND_COLOR)
        ),
        presenter_info=DrawableText(
            size=(250, 400),
            position=(1200, 1200),
            font_path=DEFAULT_FONT,
            font_size=30,
            font_color=DEFAULT_COLOR,
            text_alignment=TextAlignment.LEFT,
            text_line=TextLine.LEFT.set_line_width(DEFAULT_LINE_WIDTH),
            text_background=TextBackground.ROUNDED.set_color(DEFAULT_TEXT_BACKGROUND_COLOR)
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
            size=(1200, 200),
            position=(150, 580),
            font_path=DEFAULT_FONT_BOLD,
            font_size=65,
            font_color=DEFAULT_COLOR,
            text_alignment=TextAlignment.CENTER,
            text_line=TextLine.VERTICAL.set_line_width(DEFAULT_LINE_WIDTH)
        ),
        event_place=DrawableText(
            size=(1200, 150),
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
            "presenter": ["presenter_info", "presenter_name"],
            "time_place": ["event_time", "event_place"],
        }
    )