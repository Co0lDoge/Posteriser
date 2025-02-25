from drawable.drawable_object import DrawableText, TextAlignment, TextLine
from PIL import Image, ImageDraw, ImageFont
from typing import List

def wrap_text(text: str, style: DrawableText) -> Image.Image:
    width, height = style.size
    font_color = style.font_color
    font_path = style.font_path
    font_size = style.font_size

    # Create a transparent image
    image = Image.new("RGBA", (width, height), (255, 255, 255, 0))
    draw = ImageDraw.Draw(image)

    # Font selection with fallback
    try:
        font = ImageFont.truetype(font_path, font_size)
    except IOError:
        font = ImageFont.load_default()

    # Early return if text is empty
    if not text.strip():
        return image

    # Wrap the text into lines
    lines = wrap_text_to_lines(text, font, width, draw)
    total_text_height = len(lines) * font_size
    starting_y = 20  # Top margin

    # Draw decorative lines if specified
    if style.text_line:
        draw_decorative_lines(draw, style, starting_y, total_text_height, width)

    # Draw the text lines with alignment
    draw_text_lines(draw, lines, font, starting_y, style.text_alignment, font_color, width, font_size)

    return image

def wrap_text_to_lines(text: str, font: ImageFont.ImageFont, max_width: int, draw: ImageDraw.ImageDraw) -> List[str]:
    """Wraps the given text into lines that fit within max_width."""
    words = text.split()
    if not words:
        return []
    
    lines = []
    current_line = words[0]
    
    for word in words[1:]:
        test_line = f"{current_line} {word}"
        if draw.textlength(test_line, font=font) <= max_width:
            current_line = test_line
        else:
            lines.append(current_line)
            current_line = word
    lines.append(current_line)
    return lines

def draw_decorative_lines(draw: ImageDraw.ImageDraw, style: DrawableText, y_position: int, total_text_height: int, bbox_width: int):
    """Draws decorative lines on the image based on the style settings."""
    line_width = style.text_line.line_width
    if style.text_line == TextLine.LEFT:
        # Draw a vertical line near the left edge
        x_line = 5
        draw.line(
            [(x_line, y_position), (x_line, y_position + total_text_height)],
            fill="white",
            width=line_width,
        )
    elif style.text_line == TextLine.VERTICAL:
        # Draw horizontal lines above and below the text block
        draw.line(
            [(0, y_position - 10), (bbox_width, y_position - 10)],
            fill="white",
            width=line_width,
        )
        draw.line(
            [(0, y_position + total_text_height + 20), (bbox_width, y_position + total_text_height + 20)],
            fill="white",
            width=line_width,
        )

def draw_text_lines(
    draw: ImageDraw.ImageDraw,
    lines: List[str],
    font: ImageFont.ImageFont,
    starting_y: int,
    alignment: TextAlignment,
    text_color,
    bbox_width: int,
    font_size: int
):
    """Draws the provided lines of text onto the image with the specified alignment."""
    y_position = starting_y
    for line in lines:
        line_length = draw.textlength(line, font=font)
        if alignment == TextAlignment.CENTER:
            x_position = (bbox_width - line_length) // 2
        elif alignment == TextAlignment.LEFT:
            x_position = 20  # A left margin to avoid overlap with decorative lines
        else:
            x_position = 0  # Default fallback

        draw.text((x_position, y_position), line, font=font, fill=text_color)
        y_position += font_size