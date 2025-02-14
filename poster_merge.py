from PIL import Image, ImageDraw, ImageFont
from template.poster_template import Template
from drawable.drawable_object import DrawableImage, DrawableText

class PosterBuilder:
    def __init__(self):
        self.template: Template = None
        self.photo: Image = None
        self.background: Image = None
        self.name: str = None
        self.desc: str = None
        self.title: str = None

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
    
    def set_title(self, title: str):
        self.title = title
        return self

    def build(self) -> Image:
        builded_poster = self.background
        if self.photo != None:
            builded_poster = self.__paste_image(
                background=builded_poster,
                foreground=self.__resize_image(self.photo, height=self.template.photo.size[1]),
                style=self.template.photo
            )
        if self.desc != None:
            builded_poster = self.__paste_text(
                text=self.desc,
                background=builded_poster,
                style=self.template.description
            )
        if self.name != None:
            builded_poster = self.__paste_text(
                text=self.name,
                background=builded_poster,
                style=self.template.name
            )
        if self.title != None:
            builded_poster = self.__paste_text(
                text=self.title,
                background=builded_poster,
                style=self.template.title
            )
        return builded_poster
    
    def __paste_text(self, background: Image, text: str, style: DrawableText):
        wrapped_text_image = self.__wrap_text(text, style)

        return self.__paste_image(background, wrapped_text_image, style)
    
    def __paste_image(self, background: Image, foreground: Image, style: DrawableImage):
        background = Image.alpha_composite(
            Image.new("RGBA", background.size),
            background.convert('RGBA')
        )

        background.paste(
            foreground,
            style.position,
            foreground
        )

        return background
    
    def __wrap_text(self, text: str, style: DrawableText):
        """
        Wraps text within a bounding box and returns an image.

        Args:
            text (str): The text to wrap.
            style (DrawableText): An instance of DrawableText containing styling and layout information.

        Returns:
            Image: An image with the wrapped text.
        """
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
        
