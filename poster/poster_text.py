from drawable.drawable_object import DrawableText, TextAlignment, TextLine
from PIL import Image, ImageDraw, ImageFont

def wrap_text(text: str, style: DrawableText):
        # Extract properties from the DrawableText object
        bbox = style.size
        color = style.font_color
        font_path = style.font_path
        font_size = style.font_size

        # Create a transparent image
        image = Image.new("RGBA", bbox, (255, 255, 255, 0))
        draw = ImageDraw.Draw(image)

        # Font Selection
        try:
            font = ImageFont.truetype(font_path, font_size)  # Use the specified font
        except IOError:
            font = ImageFont.load_default()  # Fallback to default font

        # Wrap the text
        lines = []
        words = text.split()
        current_line = words[0]

        for word in words[1:]:
            # Check if adding the next word exceeds the bounding box width
            if draw.textlength(current_line + " " + word, font=font) <= bbox[0]:
                current_line += " " + word
            else:
                lines.append(current_line)
                current_line = word
        lines.append(current_line)

        # Set vertical alignment to the top 
        total_text_height = len(lines) * font_size
        y_position = 20
        
        # Draw lines if specified in style
        if style.text_line:
            if style.text_line == TextLine.LEFT:
                line_x_position = 5  # Offset from the left margin
                line_y_start = y_position
                line_y_end = y_position + total_text_height
                draw.line([(line_x_position, line_y_start), (line_x_position, line_y_end)], fill="white", width=style.text_line.line_width)
            elif style.text_line == TextLine.VERTICAL:
                line_x_start = 0
                line_x_end = bbox[0]
                draw.line([(line_x_start, y_position - 10), (line_x_end, y_position - 10)], fill="white", width=style.text_line.line_width)  # Top line
                draw.line([(line_x_start, y_position + total_text_height + 20), (line_x_end, y_position + total_text_height + 20)], fill="white", width=style.text_line.line_width)  # Bottom line

        # Draw text
        for line in lines:
            line_width = draw.textlength(line, font=font)
            match style.text_alignment:
                case TextAlignment.CENTER:
                    x_position = (bbox[0] - line_width) // 2
                case TextAlignment.LEFT:
                    x_position = 10  # Indent slightly to avoid overlap with the line

            match style.text_alignment:
                case TextAlignment.CENTER:
                    x_position = (bbox[0] - line_width) // 2
                case TextAlignment.LEFT:
                    x_position = 20

            draw.text((x_position, y_position), line, font=font, fill=color)
            y_position += font_size  # Move to the next line

        return image