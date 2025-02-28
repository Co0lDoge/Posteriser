import argparse
import ast

def load_args():
    parser = argparse.ArgumentParser(description="Load event configuration parameters.")

    parser.add_argument("--name_1", type=str, required=True, help="Name of the first participant (e.g., 'Борис Борисов')")
    parser.add_argument("--name_1_info", type=str, required=True, help="Info of the first participant (e.g., 'Генеральный директор')")
    parser.add_argument("--name_1_photo", type=str, required=True, help="Path to the first participant's photo (e.g., 'res/photo1.png')")

    parser.add_argument("--name_2", type=str, required=True, help="Name of the second participant (e.g., 'Николай Борисов')")
    parser.add_argument("--name_2_info", type=str, required=True, help="Info of the second participant (e.g., 'Диванный директор')")
    parser.add_argument("--name_2_photo", type=str, required=True, help="Path to the second participant's photo (e.g., 'res/photo2.jpg')")

    parser.add_argument("--name_3", type=str, required=True, help="Name of the third participant (e.g., 'Игорь Креслов')")
    parser.add_argument("--name_3_info", type=str, required=True, help="Info of the third participant (e.g., 'Журналист')")
    parser.add_argument("--name_3_photo", type=str, required=True, help="Path to the third participant's photo (e.g., 'res/photo3.jpg')")

    parser.add_argument("--logo", type=str, required=True, help="Path to the company logo (e.g., 'res/logo.webp')")
    parser.add_argument("--logo_info", type=str, required=True, help="Company name (e.g., 'SOMECOMPANYNAME')")

    parser.add_argument("--event_desc", type=str, required=True, help="Event description (e.g., 'Добро пожаловать на мероприятие...')")
    parser.add_argument("--event_title", type=str, required=True, help="Event title (e.g., 'Конференция по программированию')")
    parser.add_argument("--event_time", type=str, required=True, help="Event time (e.g., '25.02.25 в 21.00')")
    parser.add_argument("--event_place", type=str, required=True, help="Event place (e.g., 'г.Уфа, ул. Ибрагимова 30')")
    parser.add_argument(
        "--color_scheme", 
        type=lambda s: ast.literal_eval(s), 
        required=True, 
        help="Color scheme as a tuple, e.g., '(0, 0, 255)'"
    )

    args = parser.parse_args()

    return (
        args.name_1,
        args.name_1_info,
        args.name_1_photo,
        args.name_2,
        args.name_2_info,
        args.name_2_photo,
        args.name_3,
        args.name_3_info,
        args.name_3_photo,
        args.logo,
        args.logo_info,
        args.event_desc,
        args.event_title,
        args.event_time,
        args.event_place,
        args.color_scheme,
    )

def load_test_args():
    name_1 = "Борис Борисов"
    name_1_info = "Генеральный директор"
    name_1_photo = "res/Professional-Headshot-Poses-Blog-Post-1.png"
    name_2 = "Николай Борисов"
    name_2_info = "Диванный директор"
    name_2_photo = "res/man.jpg"
    name_3 = "Игорь Креслов"
    name_3_info = "Журналист"
    name_3_photo = "res/third.jpg"
    logo = 'res/logo.webp'
    logo_info = "OOO SOMECOMPANYNAME MEZHRAIONKA Celis"
    event_desc = "Дбро пожаловать на мераприятье на которое нихто никокда ни придед. Сдесь вас не покажут ничего и нищего ты не увидити. Возможно ничиво не происойдет. А восмошно и нет."
    event_title = "Конференция по программированию"
    event_time = "25.02.25 в 21.00"
    event_place = "г.Уфа, ул. Ибрагимова 30"
    color_scheme = (0, 0, 255)
    return (
        name_1,
        name_1_info,
        name_1_photo,
        name_2,
        name_2_info,
        name_2_photo,
        name_3,
        name_3_info,
        name_3_photo,
        logo,
        logo_info,
        event_desc,
        event_title,
        event_time,
        event_place,
        color_scheme,
    )



