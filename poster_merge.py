from PIL import Image, ImageDraw, ImageFont
import textwrap

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

        max_width = 200 # Maximum width in pixels for each line
        letter_height = font.getbbox('x')[3] - font.getbbox('x')[0]
        letter_width = font.getbbox('x')[1] - font.getbbox('x')[0]
        
        # Wrap the text
        wrapped_text = textwrap.wrap(text, width=int(max_width // letter_width))  # Adjust width based on font size

        # Define the starting position for the text
        text_position = (50, 150)
        text_color = (255, 255, 255)

        # Draw each line of the wrapped text
        y_position = text_position[1]
        for line in wrapped_text:
            draw.text((text_position[0], y_position), line, fill=text_color, font=font)
            y_position += letter_height  # Move to the next line by increasing the y-position

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