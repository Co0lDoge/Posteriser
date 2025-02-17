from dataclasses import dataclass
from enum import Enum

class TextAlignment(Enum):
    LEFT = "left"
    CENTER = "center"

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