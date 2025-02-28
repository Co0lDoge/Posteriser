from drawable.drawable_object import DrawableText, TextAlignment, TextLine, TextBackground
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

    if style.text_background == TextBackground.ROUNDED:
        draw_rounded_rectangle(draw, width, height, 20, "black")

    # Draw the text lines with alignment
    draw_text_lines(draw, lines, font, starting_y, style.text_alignment, font_color, width, font_size)

    return image

def wrap_text_group(items: List[tuple[str, DrawableText]]) -> Image.Image:
    image_list = []
    for text, style in items:
        width = style.size[0]  # Use the given width; height will be computed dynamically.
        font_color = style.font_color
        font_path = style.font_path
        font_size = style.font_size

        # Font selection with fallback
        try:
            font = ImageFont.truetype(font_path, font_size)
        except IOError:
            font = ImageFont.load_default()

        # Early check: if text is empty, create a minimal blank image.
        if not text.strip():
            blank_image = Image.new("RGBA", (width, 1), (255, 255, 255, 0))
            image_list.append(blank_image)
            continue

        # Create a dummy image (height doesn't matter here) to compute text wrapping.
        dummy_image = Image.new("RGBA", (width, 1), (255, 255, 255, 0))
        dummy_draw = ImageDraw.Draw(dummy_image)
        lines = wrap_text_to_lines(text, font, width, dummy_draw)

        # Calculate total height required for the text.
        total_text_height = len(lines) * font_size
        starting_y = 0  # Top margin (adjust if needed)
        final_height = starting_y + total_text_height

        # Now create the final image with the computed height.
        image = Image.new("RGBA", (width, final_height), (255, 255, 255, 0))
        draw = ImageDraw.Draw(image)

        # Draw the text lines with the desired alignment.
        draw_text_lines(draw, lines, font, starting_y, style.text_alignment, font_color, width, font_size)

        image_list.append(image)

    # Concatenate all the images vertically (top-aligned)
    combined_image = concat_images_vertically(image_list)
    combined_draw = ImageDraw.Draw(combined_image)
    combined_width, combined_height = combined_image.size

    first_style = items[0][1]
    if style.text_background == TextBackground.ROUNDED:
        combined_image = draw_behind_image(combined_image)

    # Draw a decorative line along the left edge of the combined image,
    # using the style from the first item (if it specifies a left decorative line).
    if first_style.text_line and first_style.text_line == TextLine.LEFT:
        # starting_y is 0 and total_text_height is the full height of the combined image.
        draw_decorative_lines(combined_draw, first_style, 0, combined_height, combined_width)

    return combined_image

def concat_images_horizontally(images: List[Image.Image]) -> Image.Image:
    """
    Concatenates a list of images horizontally.
    The resulting image's height is set to the maximum height among all images,
    and images are pasted side-by-side from left to right.
    """
    if not images:
        raise ValueError("No images to concatenate.")

    total_width = sum(image.width for image in images)
    max_height = max(image.height for image in images)
    
    # Create a new transparent image to hold the concatenated result
    result_image = Image.new("RGBA", (total_width, max_height), (255, 255, 255, 0))
    x_offset = 0

    for image in images:
        result_image.paste(image, (x_offset, 0), image)
        x_offset += image.width

    return result_image

def concat_images_vertically(images: List[Image.Image]) -> Image.Image:
    """
    Concatenates a list of images vertically.
    The resulting image's width is set to the maximum width among all images,
    and images are pasted from top to bottom.
    """
    if not images:
        raise ValueError("No images to concatenate.")

    max_width = max(image.width for image in images)
    total_height = sum(image.height for image in images)
    
    # Create a new transparent image to hold the concatenated result
    result_image = Image.new("RGBA", (max_width, total_height), (255, 255, 255, 0))
    y_offset = 0

    for image in images:
        result_image.paste(image, (0, y_offset), image)
        y_offset += image.height

    return result_image

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

def draw_rounded_rectangle(draw, width, height, radius, color):    
    # Define corner points
    left, top, right, bottom = 0, 0, width, height
    
    # Draw rounded rectangle using pieslice and rectangles
    draw.pieslice([left, top, left + 2 * radius, top + 2 * radius], 180, 270, fill=color)
    draw.pieslice([right - 2 * radius, top, right, top + 2 * radius], 270, 360, fill=color)
    draw.pieslice([left, bottom - 2 * radius, left + 2 * radius, bottom], 90, 180, fill=color)
    draw.pieslice([right - 2 * radius, bottom - 2 * radius, right, bottom], 0, 90, fill=color)
    
    # Draw rectangles to connect the corners
    draw.rectangle([left + radius, top, right - radius, bottom], fill=color)
    draw.rectangle([left, top + radius, right, bottom - radius], fill=color)

    from PIL import Image, ImageDraw

def draw_behind_image(combined_image: Image.Image, background_color=(0, 0, 0, 255)) -> Image.Image:
    combined_width, combined_height = combined_image.size
    padding = 10  # Adjust padding if needed

    # Check if the background color has transparency (RGBA)
    has_transparency = len(background_color) == 4
    mode = "RGBA" if has_transparency else "RGB"

    # Create a new transparent image with padding
    background = Image.new(mode, (combined_width + 2 * padding, combined_height + 2 * padding), (0, 0, 0, 0))

    # Draw rounded rectangle on the background
    background_draw = ImageDraw.Draw(background)
    draw_rounded_rectangle(background_draw, background.width, background.height, 20, background_color)

    # Paste the combined image on top of the background
    background.paste(combined_image, (padding, padding), combined_image if "A" in combined_image.mode else None)

    return background