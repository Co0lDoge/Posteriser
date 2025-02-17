from dataclasses import dataclass
from enum import Enum

class TextAlignment(Enum):
    LEFT = "left"
    CENTER = "center"

@dataclass
class DrawableImage():
    size: tuple
    position: tuple

@dataclass
class DrawableText:
    size: tuple
    position: tuple
    font_path: str
    font_size: tuple
    font_color: tuple
    text_alignment: TextAlignment