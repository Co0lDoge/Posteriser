class DrawableImage():
    def __init__(self, size, position):
        self.size = size
        self.position = position

class DrawableText:
    def __init__(self, size, position, font_path, font_size, font_color):
        self.size = size
        self.position = position
        self.font_path = font_path
        self.font_size = font_size
        self.font_color = font_color