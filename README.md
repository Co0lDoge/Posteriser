# Poster Generator
> [!IMPORTANT]
> Генератор использует модели нейросетей для исправления текста и удаления фона изображений

## Запуск
```sh
python main.py 
  --name_1 "Борис Борисов" --name_1_info "Генеральный директор" --name_1_photo "res/photo1.png" 
  --name_2 "Николай Борисов" --name_2_info "Диванный директор" --name_2_photo "res/photo2.jpg" 
  --name_3 "Игорь Креслов" --name_3_info "Журналист" --name_3_photo "res/photo3.jpg" 
  --logo "res/logo.webp" --logo_info "SOMECOMPANYNAME" 
  --event_desc "Добро пожаловать на мероприятие..." 
  --event_title "Конференция по программированию" 
  --event_time "25.02.25 в 21.00" --event_place "г.Уфа, ул. Ибрагимова 30"
  --color_scheme "(0, 0, 255)"
```
## Пример генерации
![image](https://github.com/user-attachments/assets/62653658-9954-46fe-a904-c5dbd8bdfb07)
