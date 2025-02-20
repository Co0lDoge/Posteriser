from dataclasses import dataclass
from enum import Enum

class TextAlignment(Enum):
    LEFT = "left"
    CENTER = "center"

class TextLine(Enum):
    LEFT = "left"
    VERTICAL = "vertical"

    def __init__(self, value):
        self._value_ = value
        self.line_width = 2

    def set_line_width(self, line_width):
        self.line_width = line_width
        return self

@dataclass
class DrawableImage():
    size: tuple[int, int]
    position: tuple[int, int]

@dataclass
class DrawableText:
    size: tuple[int, int]
    position: tuple[int, int]
    font_path: str
    font_size: int
    font_color: tuple[int, int, int]
    text_alignment: TextAlignment
    text_line: TextLine = None