from PIL import Image, ImageDraw, ImageFont
from PIL.Image import Image as ImageType
from template.poster_template import Template
from drawable.drawable_object import DrawableImage, DrawableText, TextAlignment

from typing import Optional

class PosterBuilder:
    def __init__(self):
        self.template: Optional[Template] = None
        self.photo: Optional[ImageType] = None
        self.logo: Optional[ImageType] = None
        self.background: Optional[ImageType] = None
        self.name: Optional[str] = None
        self.description: Optional[str] = None
        self.title: Optional[str] = None

    def set_template(self, template: Template) -> "PosterBuilder":
        self.template = template
        return self

    def set_background(self, background: ImageType) -> "PosterBuilder":
        self.background = background
        return self

    def set_description(self, description: str) -> "PosterBuilder":
        self.description = description
        return self
    
    def set_name(self, name: str) -> "PosterBuilder":
        self.name = name
        return self
    
    def set_name_info(self, name_info: str) -> "PosterBuilder":
        self.name_info = name_info
        return self
    
    def set_photo(self, photo: ImageType) -> "PosterBuilder":
        self.photo = photo
        return self
    
    def set_logo(self, logo: ImageType) -> "PosterBuilder":
        self.logo = logo
        return self
    
    def set_title(self, title: str) -> "PosterBuilder":
        self.title = title
        return self

    def build(self) -> ImageType:
        if self.background is None:
            raise ValueError("Background must be set before building the poster.")
        if self.template is None:
            raise ValueError("Template must be set before building the poster.")

        poster = self.background.copy()

        # Map each image field to its corresponding style from the template
        image_fields = [
            (self.photo, self.template.photo),
            (self.logo, self.template.logo)
        ]

        # Map each text field to its corresponding style from the template
        text_fields = [
            (self.description, self.template.description),
            (self.name, self.template.name),
            (self.name_info, self.template.name_info),
            (self.title, self.template.title)
        ]

        for image, style in image_fields:
            if image is not None:
                resized_image = self.__resize_image(image, size=style.size)
                poster = self.__paste_image(
                    background=poster,
                    foreground=resized_image,
                    style=style
            )

        for text, style in text_fields:
            if text is not None:
                poster = self.__paste_text(
                    text=text,
                    background=poster,
                    style=style
                )
        return poster
    
    def __paste_text(self, background: ImageType, text: str, style: DrawableText):
        wrapped_text_image = self.__wrap_text(text, style)

        return self.__paste_image(background, wrapped_text_image, style)
    
    def __paste_image(self, background: ImageType, foreground: ImageType, style: DrawableImage):
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

        for line in lines:
            line_width = draw.textlength(line, font=font)

            match style.text_alignment:
                case TextAlignment.CENTER:
                    x_position = (bbox[0] - line_width) // 2
                case TextAlignment.LEFT:
                    x_position = 0

            draw.text((x_position, y_position), line, font=font, fill=color)
            y_position += font_size  # Move to the next line

        return image
    
    def __resize_image(self, image: ImageType, size: tuple[int, int]):
        # Get the original dimensions
        original_width, original_height = image.size

        width, height = size

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
        
