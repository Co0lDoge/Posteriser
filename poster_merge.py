from PIL import Image, ImageDraw, ImageFont
from PIL.Image import Image as ImageType
from template.poster_template import Template
from drawable.drawable_object import DrawableImage, DrawableText, TextAlignment, TextLine

from typing import Optional

POSTER_DEBUG = False

class PosterBuilder:
    def __init__(self):
        self.template: Optional[Template] = None
        self.photo: Optional[ImageType] = None
        self.logo: Optional[ImageType] = None
        self.logo_info: Optional[str] = None
        self.background: Optional[ImageType] = None
        self.name: Optional[str] = None
        self.event_description: Optional[str] = None
        self.event_title: Optional[str] = None
        self.event_time: Optional[str] = None
        self.event_place: Optional[str] = None

    def set_template(self, template: Template) -> "PosterBuilder":
        self.template = template
        return self

    def set_background(self, background: ImageType) -> "PosterBuilder":
        self.background = background
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
    
    def set_logo_info(self, logo_info: str) -> "PosterBuilder":
        self.logo_info = logo_info
        return self
    
    def set_event_title(self, title: str) -> "PosterBuilder":
        self.event_title = title
        return self
    
    def set_event_description(self, description: str) -> "PosterBuilder":
        self.event_description = description
        return self
    
    def set_event_time(self, time: str) -> "PosterBuilder":
        self.event_time = time
        return self
    
    def set_event_place(self, place: str) -> "PosterBuilder":
        self.event_place = place
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
            (self.name, self.template.name),
            (self.name_info, self.template.name_info),
            (self.logo_info, self.template.logo_info),
            (self.event_description, self.template.event_description),
            (self.event_title, self.template.event_title),
            (self.event_time, self.template.event_time),
            (self.event_place, self.template.event_place),
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

        if POSTER_DEBUG:
            debug_bbox = Image.new("RGBA", foreground.size, (255, 0, 0, 128))
            background.paste(
            debug_bbox,
            style.position,
            debug_bbox
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

        # Set vertical alignment to the top 
        total_text_height = len(lines) * font_size
        y_position = 20
        
        # Draw lines if specified in style
        if style.text_line:
            if style.text_line == TextLine.LEFT:
                line_x_position = 5  # Offset from the left margin
                line_y_start = y_position
                line_y_end = y_position + total_text_height
                draw.line([(line_x_position, line_y_start), (line_x_position, line_y_end)], fill="white", width=2)
            elif style.text_line == TextLine.VERTICAL:
                line_x_start = 0
                line_x_end = bbox[0]
                draw.line([(line_x_start, y_position - 10), (line_x_end, y_position - 10)], fill="white", width=2)  # Top line
                draw.line([(line_x_start, y_position + total_text_height + 20), (line_x_end, y_position + total_text_height + 20)], fill="white", width=2)  # Bottom line

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
        
