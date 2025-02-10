from PIL import Image, ImageDraw, ImageFont

def merge_content(background, photo, name, text):
    photo_position = (0, 900 - 400)
    background.paste(photo, photo_position)

    # Drawing the name and corrected text
    draw = ImageDraw.Draw(background)

    # You can use a default font or specify a custom one
    try:
        font = ImageFont.truetype("arial.ttf", 40)  # Change font and size as needed
    except IOError:
        font = ImageFont.load_default()  # Fallback to default font

    # Set up text positions
    name_position = (50, 50)  # Customize position as needed
    text_position = (50, 150)  # Customize position as needed

    # Choose color for the text
    text_color = (255, 255, 255)  # White color for text

    # Add name and corrected text to the image
    draw.text(name_position, name, fill=text_color, font=font)
    draw.text(text_position, text, fill=text_color, font=font)

    return background