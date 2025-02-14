class Template:
    def __init__(
        self,
        background_size,
        photo_height,
        photo_position,

        desc_bbox,
        desc_position,
        desc_font_path,
        desc_font_size,
        desc_color,

        name_bbox,
        name_position,  
        name_font_path,  
        name_font_size,  
        name_color,  
    ):        
        self.background_size = background_size
        self.photo_height = photo_height
        self.photo_position = photo_position

        self.desc_bbox = desc_bbox
        self.desc_position = desc_position
        self.desc_font_path = desc_font_path
        self.desc_font_size = desc_font_size
        self.desc_color = desc_color

        self.name_bbox = name_bbox
        self.name_position = name_position
        self.name_font_path = name_font_path
        self.name_font_size = name_font_size
        self.name_color = name_color

    def get_default_template():
        return Template(
            background_size = 900,
            photo_height = 600,
            photo_position = (0, 900-600),

            desc_bbox = (400, 200),
            desc_position = (400, 200),
            desc_font_path = "arial.ttf",
            desc_font_size = 40,
            desc_color = (255, 255, 255),

            name_bbox = (220, 100),
            name_position = (330, 570),
            name_font_path = "arial.ttf",
            name_font_size = 40,
            name_color = (255, 255, 255),
        )