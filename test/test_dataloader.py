import subprocess

# List of configurations
configurations = [
    {
        "name_1": "Борис Борисов",
        "name_1_info": "Генеральный директор",
        "name_1_photo": "./res/photo1.png",
        "name_2": "Николай Борисов",
        "name_2_info": "Диванный директор",
        "name_2_photo": "./res/photo2.jpg",
        "name_3": "Игорь Креслов",
        "name_3_info": "Журналист",
        "name_3_photo": "./res/photo3.jpg",
        "logo": "./res/logo.webp",
        "logo_info": "SOMECOMPANYNAME",
        "event_desc": "Добро пожаловать на мероприятие...",
        "event_title": "Конференция по программированию",
        "event_time": "25.02.25 в 21.00",
        "event_place": "г.Уфа, ул. Ибрагимова 30",
        "color_scheme": "(0, 0, 255)",
        "output_path": "output/event1.png"
    },
    {
        "name_1": "Алексей Смирнов",
        "name_1_info": "Разработчик Python",
        "name_1_photo": "./res/photo1.png",
        "name_2": "Дмитрий Иванов",
        "name_2_info": "Менеджер проектов",
        "name_2_photo": "./res/photo2.jpg",
        "name_3": "Сергей Козлов",
        "name_3_info": "Дизайнер",
        "name_3_photo": "./res/photo3.jpg",
        "logo": "./res/logo.webp",
        "logo_info": "ANOTHERCOMPANY",
        "event_desc": "Техническая конференция для IT-специалистов...",
        "event_title": "IT Meetup 2025",
        "event_time": "10.03.25 в 15.00",
        "event_place": "Москва, ул. Ленина 1",
        "color_scheme": "(255, 0, 0)",
        "output_path": "output/event2.png"
    },
    {
        "name_1": "Мария Крылова",
        "name_1_info": "Тестировщик",
        "name_1_photo": "./res/photo1.png",
        "name_2": "Василий Сидоров",
        "name_2_info": "DevOps инженер",
        "name_2_photo": "./res/photo2.jpg",
        "name_3": None,
        "name_3_info": None,
        "name_3_photo": None,
        "logo": "./res/logo.webp",
        "logo_info": "HRTECH",
        "event_desc": "Как построить карьеру в IT?",
        "event_title": "HR & IT Forum",
        "event_time": "15.04.25 в 18.00",
        "event_place": "Москва, Невский 45",
        "color_scheme": "(0, 255, 0)",
        "output_path": "output/event3.png"
    },
    {
        "name_1": "Иван Тарасов",
        "name_1_info": "Машинное обучение",
        "name_1_photo": "./res/photo1.png",
        "name_2": None,
        "name_2_info": None,
        "name_2_photo": None,
        "name_3": None,
        "name_3_info": None,
        "name_3_photo": None,
        "logo": "./res/logo.webp",
        "logo_info": "AICOMPANY",
        "event_desc": "Будущее искусственного интеллекта...",
        "event_title": "AI & ML Summit",
        "event_time": "20.05.25 в 12.00",
        "event_place": "Казань, ул. Баумана 10",
        "color_scheme": "(128, 0, 128)",
        "output_path": "output/event4.png"
    },

    # Long text
    {
        "name_1": "Алексей Смирнов",
        "name_1_info": "Разработчик Python",
        "name_1_photo": "./res/photo1.png",
        "name_2": "Дмитрий Иванов",
        "name_2_info": "Менеджер проектов",
        "name_2_photo": "./res/photo2.jpg",
        "name_3": "Сергей Козлов",
        "name_3_info": "Дизайнер",
        "name_3_photo": "./res/photo3.jpg",
        "logo": "./res/logo.webp",
        "logo_info": "ANOTHERCOMPANY in the woods why am I writing this",
        "event_desc": "Техническая конференция для IT-специалистов и всех, кто интересуется новыми технологиями и трендами в IT-индустрии. Мы приглашаем вас на IT Meetup 2025, который состоится 10 марта 2025 года в Москве. На мероприятии вы сможете встретиться с лучшими специалистами отраслию",
        "event_title": "IT Meetup 2025",
        "event_time": "10.03.25 в 15.00",
        "event_place": "Москва, ул. Ленина 1",
        "color_scheme": "(21, 0, 245)",
        "output_path": "output/event5.png"
    },
    {
        "name_1": "Мария Крылова",
        "name_1_info": "Тестировщик",
        "name_1_photo": "./res/photo1.png",
        "name_2": "Василий Сидоров",
        "name_2_info": "DevOps инженер",
        "name_2_photo": "./res/photo2.jpg",
        "name_3": None,
        "name_3_info": None,
        "name_3_photo": None,
        "logo": "./res/logo.webp",
        "logo_info": "HRTECH lorem ipsun bolor is losum ivek",
        "event_desc": "Как построить карьеру в IT? Какие навыки нужны для успешной карьеры в IT? Какие тенденции будут актуальны в ближайшие годы? На эти и другие вопросы ответят специалисты на нашем мероприятии.",
        "event_title": "HR & IT Forum",
        "event_time": "15.04.25 в 18.00",
        "event_place": "Санкт-Петербург, пр. Невский 45",
        "color_scheme": "(0, 120, 120)",
        "output_path": "output/event6.png"
    },
    {
        "name_1": "Иван Тарасов",
        "name_1_info": "Машинное обучение",
        "name_1_photo": "./res/photo1.png",
        "name_2": None,
        "name_2_info": None,
        "name_2_photo": None,
        "name_3": None,
        "name_3_info": None,
        "name_3_photo": None,
        "logo": "./res/logo.webp",
        "logo_info": "AICOMPANY Nocompany lorem ipsun dolor sit amet",
        "event_desc": "Будущее искусственного интеллекта и машинного обучения. Какие технологии будут актуальны в ближайшие годы? Какие проблемы стоят перед разработчиками? На эти вопросы ответят специалисты на нашем мероприятии.",
        "event_title": "AI & ML Summit",
        "event_time": "20.05.25 в 12.00",
        "event_place": "Казань, ул. Баумана 10",
        "color_scheme": "(64, 20, 150)",
        "output_path": "output/event7.png"
    }
]

# Run the script 4 times with different configurations
for config in configurations:
    cmd = [
        "C:/WorkFolder/ML/Posteriser/.venv/Scripts/python.exe", "./main.py"
    ]
    
    # Loop through the config items and add only if the value is not None.
    for key, value in config.items():
        if value is not None:
            cmd.extend([f"--{key}", str(value)])

    # Run the subprocess
    subprocess.run(cmd)
