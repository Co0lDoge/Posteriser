from PIL import Image, ImageDraw, ImageFont, ImageOps
import textwrap

class PosterGenerator:
    templates = None

    def merge_content(self, background, photo, name, text):
        width = 400
        height = 600
        photo_position = (0, 900 - height)
        photo = self.__resize_image(photo, height=height)
        
        bbox = (400, 200)  # Width and height of the bounding box
        text = "This is a sample text that will be wrapped into the bounding box."
        color = (255, 255, 255)  # Black text
        font_path = "arial.ttf"
        font_size = 40

        background = self.paste_image(background, photo, photo_position)
        background = self.paste_text(background, bbox, text, color, font_path, font_size)
        return background

    def paste_text(self, background: Image, bbox: tuple, text: str, color: tuple, font_path: str, font_size: int):
        wrapped_text_image = self.wrap_text(bbox, text, color, font_path, font_size)

        return self.paste_image(background, wrapped_text_image, bbox)
    
    def paste_image(self, background: Image, foreground: Image, position: tuple):
        background = Image.alpha_composite(
            Image.new("RGBA", background.size),
            background.convert('RGBA')
        )

        background.paste(
            foreground,
            position,
            foreground
        )

        return background
    
    def wrap_text(self, bbox: tuple, text: str, color: tuple, font_path: str, font_size: int):
        # Create a blank image with a transparent background
        image = Image.new("RGBA", bbox, (255, 255, 255, 0))
        draw = ImageDraw.Draw(image)

        # Font Selection
        try:
            font = ImageFont.truetype(font_path, font_size)  # Change font and size as needed
        except IOError:
            font = ImageFont.load_default()  # Fallback to default font

        lines = []
        words = text.split()
        current_line = words[0]

        # Wrap the text
        for word in words[1:]:
            # Check if adding the next word exceeds the bounding box width
            if draw.textlength(current_line + " " + word, font=font) <= bbox[0]:
                current_line += " " + word
            else:
                lines.append(current_line)
                current_line = word
        lines.append(current_line)

        # Calculate starting y-position to center the text vertically
        total_text_height = len(lines) * font_size
        y_position = (bbox[1] - total_text_height) // 2

        # Draw each line of text
        for line in lines:
            # Calculate x-position to center the text horizontally
            line_width = draw.textlength(line, font=font)
            x_position = (bbox[0] - line_width) // 2
            draw.text((x_position, y_position), line, font=font, fill=color)
            y_position += font_size  # Move to the next line

        return image
    
    def __resize_image(self, image, width=None, height=None):
        # Get the original dimensions
        original_width, original_height = image.size

        # If both width and height are None, return the original image
        if width is None and height is None:
            return image

        # Calculate the new dimensions while maintaining the aspect ratio
        if width is None:
            # Calculate the width based on the desired height
            aspect_ratio = original_width / original_height
            width = int(height * aspect_ratio)
        elif height is None:
            # Calculate the height based on the desired width
            aspect_ratio = original_height / original_width
            height = int(width * aspect_ratio)

        # Resize the image with the computed dimensions
        resized_image = image.resize((width, height), Image.LANCZOS)

        return resized_image
    
class Template:
    def __init__(self, photo_bbox, text_bbox, text_font, text_color):
        self.photo_bbox = photo_bbox
        self.text_bbox = text_bbox
        self.text_font = text_font
        self.text_color = text_color

class PosterBuilder:
    def set_template(self, template: Template):
        self.template = template

    def set_background(self, background: Image):
        self.background = background

    def set_text(self, text: str, bbox: tuple):
        self.text = text

    def build(self) -> Image:
        pass
        
