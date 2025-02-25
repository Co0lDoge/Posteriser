from PIL import Image
from PIL.Image import Image as ImageType
from template.poster_template import Template
from drawable.drawable_object import DrawableImage, DrawableText
from poster.poster_image import resize_image
from poster.poster_text import wrap_text, wrap_text_group

from typing import Optional

class PosterBuilder:
    def __init__(self, debug: bool):
        self.template: Optional[Template] = None
        self.speaker_photo: Optional[ImageType] = None
        self.speaker_name: Optional[str] = None
        self.speaker_info: Optional[str] = None
        self.moderator_photo: Optional[ImageType] = None
        self.moderator_name: Optional[str] = None
        self.moderator_info: Optional[str] = None
        self.logo: Optional[ImageType] = None
        self.logo_info: Optional[str] = None
        self.background: Optional[ImageType] = None
        self.overlay: Optional[ImageType] = None
        self.event_description: Optional[str] = None
        self.event_title: Optional[str] = None
        self.event_time: Optional[str] = None
        self.event_place: Optional[str] = None
        self.debug = debug

    def set_template(self, template: Template) -> "PosterBuilder":
        self.template = template
        return self

    def set_background(self, background: ImageType) -> "PosterBuilder":
        self.background = background
        return self
    
    def set_overlay(self, overlay: ImageType) -> "PosterBuilder":
        self.overlay = overlay
        return self
    
    def set_speaker_name(self, name: str) -> "PosterBuilder":
        self.speaker_name = name
        return self
    
    def set_speaker_info(self, name_info: str) -> "PosterBuilder":
        self.speaker_info = name_info
        return self
    
    def set_speaker_photo(self, photo: ImageType) -> "PosterBuilder":
        self.speaker_photo = photo
        return self
    
    def set_moderator_name(self, name: str) -> "PosterBuilder":
        self.moderator_name = name
        return self
    
    def set_moderator_info(self, name_info: str) -> "PosterBuilder":
        self.moderator_info = name_info
        return self
    
    def set_moderator_photo(self, photo: ImageType) -> "PosterBuilder":
        self.moderator_photo = photo
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
            (self.speaker_photo, self.template.speaker_photo),
            (self.moderator_photo, self.template.moderator_photo),
            (self.logo, self.template.logo)
        ]

        # Map each text field to its corresponding style from the template
        text_fields = [
            (self.speaker_name, self.template.speaker_name),
            (self.speaker_info, self.template.speaker_info),
            (self.moderator_name, self.template.moderator_name),
            (self.moderator_info, self.template.moderator_info),
            (self.logo_info, self.template.logo_info),
            (self.event_description, self.template.event_description),
            (self.event_title, self.template.event_title),
            (self.event_time, self.template.event_time),
            (self.event_place, self.template.event_place),
        ]

        if self.template.groups is not None:
            text_groups = [
                group for group in [
                    [
                        (getattr(self, attr), getattr(self.template, attr)) 
                        for attr in group 
                        if getattr(self, attr) is not None
                    ]
                    for group in self.template.groups.values()
                ] if group  # Keep only non-empty groups
            ]

            # Flatten text_groups to create a set of items to remove from text_fields
            grouped_items = [item for group in text_groups for item in group]

            # Filter text_fields by removing any item that appears in grouped_items
            text_fields = [item for item in text_fields if item not in grouped_items]
        else:
            text_groups = None

        for image, style in image_fields:
            if image is not None and style is not None: # TODO: Remove style is not None
                resized_image = resize_image(image, size=style.size)
                poster = self.__paste_image(
                    background=poster,
                    foreground=resized_image,
                    style=style
            )
                
        if self.overlay is not None:
            poster = self.__paste_image(
                background=poster,
                foreground=self.overlay,
                style=DrawableImage(self.template.background_size, (0, 0))
            )
        
        for image, style in image_fields:
            if image is not None and style is not None and style.overlay: # TODO: Remove style is not None
                resized_image = resize_image(image, size=style.size)
                poster = self.__paste_image(
                    background=poster,
                    foreground=resized_image,
                    style=style
            )

        for text, style in text_fields:
            if text is not None and style is not None: # TODO: Remove style is not None
                poster = self.__paste_text(
                    text=text,
                    background=poster,
                    style=style
                )
        
        if text_groups is not None:
            for group in text_groups:
                poster = self.__paste_text_group(
                    group=group,
                    background=poster
                )
        
        return poster
    
    def __paste_text_group(self, group: list[tuple[str, DrawableText]], background: ImageType):
        wrap_text_group_image = wrap_text_group(group)

        return self.__paste_image(background, wrap_text_group_image, group[0][1])
    
    def __paste_text(self, background: ImageType, text: str, style: DrawableText):
        wrapped_text_image = wrap_text(text, style)

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

        if self.debug:
            debug_bbox = Image.new("RGBA", foreground.size, (255, 0, 0, 128))
            background.paste(
            debug_bbox,
            style.position,
            debug_bbox
        )

        return background
        
