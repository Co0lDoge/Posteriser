from drawable.drawable_object import DrawableImage, DrawableText

class Template:
    def __init__(
        self,
        background_size: int,
        photo: DrawableImage,
        description: DrawableText,
        name: DrawableText,
    ):        
        self.background_size = background_size
        self.photo = photo
        self.description = description
        self.name = name

    def get_default_template():
        return Template(
            background_size=900,
            photo=DrawableImage(
                size=(None, 600),
                position=(0, 900-600),
            ),
            description=DrawableText(
                size=(400, 200),
                position=(400, 200),
                font_path="arial.ttf",
                font_size=40,
                font_color=(255, 255, 255),
            ),
            name=DrawableText(
                size=(220, 100),
                position=(330, 570),
                font_path="arial.ttf",
                font_size=40,
                font_color=(255, 255, 255),
            )
        )