from dataclasses import dataclass

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