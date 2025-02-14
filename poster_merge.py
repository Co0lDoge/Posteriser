from PIL import Image, ImageDraw, ImageFont
from template.poster_template import Template

class PosterBuilder:
    def __init__(self):
        self.template = None
        self.photo = None
        self.background = None
        self.name = None
        self.desc = None

    def set_template(self, template: Template):
        self.template = template
        return self

    def set_background(self, background: Image):
        self.background = background
        return self

    def set_desc(self, desc: str):
        self.desc = desc
        return self
    
    def set_name(self, name: str):
        self.name = name
        return self
    
    def set_photo(self, photo: str):
        self.photo = photo
        return self

    def build(self) -> Image:
        builded_poster = self.background
        if self.photo != None:
            builded_poster = self.__paste_image(
                background=builded_poster,
                foreground=self.__resize_image(self.photo, height=self.template.photo_height),
                position=self.template.photo_position
            )
        if self.desc != None:
            builded_poster = self.__paste_text(
                background=builded_poster,
                text_bbox=self.template.desc_bbox,
                position=self.template.desc_position,
                text=self.desc,
                color=self.template.desc_color,
                font_path=self.template.desc_font_path,
                font_size=self.template.desc_font_size
            )
        if self.name != None:
            builded_poster = self.__paste_text(
                background=builded_poster,
                text_bbox=self.template.name_bbox,
                position=self.template.name_position,
                text=self.name,
                color=self.template.name_color,
                font_path=self.template.name_font_path,
                font_size=self.template.name_font_size
            )
        return builded_poster
    
    def __paste_text(self, background: Image, text_bbox: tuple, position: tuple, text: str, color: tuple, font_path: str, font_size: int):
        wrapped_text_image = self.__wrap_text(text_bbox, text, color, font_path, font_size)

        return self.__paste_image(background, wrapped_text_image, position)
    
    def __paste_image(self, background: Image, foreground: Image, position: tuple):
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
    
    def __wrap_text(self, bbox: tuple, text: str, color: tuple, font_path: str, font_size: int):
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
        
