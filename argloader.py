import argparse
import ast

def load_args():
    parser = argparse.ArgumentParser(description="Load event configuration parameters.")

    parser.add_argument("--name_1", type=str, required=False, help="Name of the first participant (e.g., 'Борис Борисов')")
    parser.add_argument("--name_1_info", type=str, required=False, help="Info of the first participant (e.g., 'Генеральный директор')")
    parser.add_argument("--name_1_photo", type=str, required=False, help="Path to the first participant's photo (e.g., 'res/photo1.png')")

    parser.add_argument("--name_2", type=str, required=False, help="Name of the second participant (e.g., 'Николай Борисов')")
    parser.add_argument("--name_2_info", type=str, required=False, help="Info of the second participant (e.g., 'Диванный директор')")
    parser.add_argument("--name_2_photo", type=str, required=False, help="Path to the second participant's photo (e.g., 'res/photo2.jpg')")

    parser.add_argument("--name_3", type=str, required=False, help="Name of the third participant (e.g., 'Игорь Креслов')")
    parser.add_argument("--name_3_info", type=str, required=False, help="Info of the third participant (e.g., 'Журналист')")
    parser.add_argument("--name_3_photo", type=str, required=False, help="Path to the third participant's photo (e.g., 'res/photo3.jpg')")

    parser.add_argument("--logo", type=str, required=False, help="Path to the company logo (e.g., 'res/logo.webp')")
    parser.add_argument("--logo_info", type=str, required=False, help="Company name (e.g., 'SOMECOMPANYNAME')")

    parser.add_argument("--event_desc", type=str, required=False, help="Event description (e.g., 'Добро пожаловать на мероприятие...')")
    parser.add_argument("--event_title", type=str, required=False, help="Event title (e.g., 'Конференция по программированию')")
    parser.add_argument("--event_time", type=str, required=False, help="Event time (e.g., '25.02.25 в 21.00')")
    parser.add_argument("--event_place", type=str, required=False, help="Event place (e.g., 'г.Уфа, ул. Ибрагимова 30')")
    parser.add_argument(
        "--color_scheme", 
        type=lambda s: ast.literal_eval(s), 
        required=True, 
        help="Color scheme as a tuple, e.g., '(0, 0, 255)'"
    )
    parser.add_argument("--output_path", type=str, required=True)

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
        args.output_path
    )
