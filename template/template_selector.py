from template.poster_template import Template
from template.templates import template_dualman, template_singleman, template_noman

def select_template(
    speaker_name:str,
    speaker_info:str,
    speaker_photo:str,
    moderator_name:str,
    moderator_info:str,
    moderator_photo:str,
) -> Template:
    is_speaker_present = speaker_name or speaker_info or speaker_photo
    is_moderator_present = moderator_name or moderator_info or moderator_photo

    if (is_speaker_present and is_moderator_present):
        return template_dualman.get_template_dualman()
    elif (is_speaker_present or is_moderator_present):
        return template_singleman.get_template_singleman()
    else:
        return template_noman.get_template_noman()
    