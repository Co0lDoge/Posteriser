from template.poster_template import Template
from template.templates import template_dualman, template_dualman_longtext, template_noman_longtext, template_singleman, template_noman, template_singleman_longtext, template_threeman
from template.templates import template_threeman_longtext

def select_template(
    speaker_name:str,
    speaker_info:str,
    speaker_photo:str,
    moderator_name:str,
    moderator_info:str,
    moderator_photo:str,
    presenter_name:str,
    presenter_info:str,
    presenter_photo:str,
    logo_info:str,
    event_place:str,
) -> Template:
    is_speaker_present = speaker_name or speaker_info or speaker_photo
    is_moderator_present = moderator_name or moderator_info or moderator_photo
    is_presenter_present = presenter_name or presenter_info or presenter_photo

    is_long_text = len(logo_info) > 20 or len(event_place) > 30

    if is_speaker_present and is_moderator_present and is_presenter_present:
        template = template_threeman_longtext.get_template_threeman if is_long_text else template_threeman.get_template_threeman
    elif is_speaker_present and is_moderator_present:
        template = template_dualman_longtext.get_template_dualman if is_long_text else template_dualman.get_template_dualman
    elif is_speaker_present or is_moderator_present:
        template = template_singleman_longtext.get_template_singleman if is_long_text else template_singleman.get_template_singleman
    else:
        template = template_noman_longtext.get_template_noman if is_long_text else template_noman.get_template_noman

    return template()
    