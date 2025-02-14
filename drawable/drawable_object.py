class DrawableImage():
    def __init__(self, photo_height, photo_position):
        self.photo_height = photo_height
        self.photo_position = photo_position

class DrawableText:
    def __init__(self, text_size, text_position, font_path, font_size, font_color):
        self.text_size = text_size
        self.text_position = text_position
        self.font_path = font_path
        self.font_size = font_size
        self.font_color = font_color