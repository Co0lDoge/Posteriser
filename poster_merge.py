from PIL import Image, ImageDraw, ImageFont

class PosterGenerator:
    templates = None

    def merge_content(self, background, photo, name, text):
        photo_position = (0, 900 - 400)
        background = self.paste_image(background, photo, photo_position)

        # Drawing the name and corrected text
        draw = ImageDraw.Draw(background)

        # Font Selection
        try:
            font = ImageFont.truetype("arial.ttf", 40)  # Change font and size as needed
        except IOError:
            font = ImageFont.load_default()  # Fallback to default font

        name_position = (50, 50)
        text_position = (50, 150)
        text_color = (255, 255, 255)

        draw.text(name_position, name, fill=text_color, font=font)
        draw.text(text_position, text, fill=text_color, font=font)

        return background

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
    
class Template:
    # Class that represents a template for a poster
    pass