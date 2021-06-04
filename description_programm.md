# FAQ
### Перед использование заполни файл settings.config.py
### Дерево проекта
```html
-Vkbot
------model
-----------bots_logic
---------------------bots_logic.py
---------------------bots_logic_event_text.py
---------------------bots_menu.py
-----------database
---------------------create_table.py
---------------------database.py
-----------keyboard
---------------------keyboard.py
-----------settings
---------------------config.py
---------------------settings_bot.py
-----------vk_user
---------------------community_msg.py
---------------------regular_expression.py
---------------------vk_user.py
------tests
-----------__init__.py
-----------tests_keyboard.py
-----------tests_regular_expression.py
------.gitignore
------description_programm.md
------group_settings.md
------README.md
------requirements.txt
------main.py
```
### Описание model.bots_logic
### здесь лежит вся логика бота
1 bots_logic.py - бесконечный цикл, слушатель, проверки для бота
* extended_city = "", extended_age = "", extended_sex = "", extended_status = "" - переменные в которые сохраняется введенная информация от пользователя
* user_id = users_db.select_users(event) - id пользователя кто пишет боту
* users_db.insert_advanced_search - если указаны данные от пользователя, добавляем в базу
* advanced_search = users_db.select_advanced_search(user_id) - получаем данные из расширенного поиска для пользователя
* result = vk_session.method("messages.getById", - использовал его потому что работает лучше чем event.text
* result_text - текст от пользователя "введенный"

2 bots_logic_event_text.py - дополнительная информация для работы бота и функция поиска
* Функция поиска работает так, если поиск по параметрам то значение беруться от пользователя
если быстрый поиск то на основании пользователя, дальше при помощи функции поиска получаем список id
у которых профиль открыт, и выдаем в выдаче, если нравиться или не нравиться записываем в базу,
и на следущей итерации сравниваем если есть такие уже то выдаем других (id)

3 bots_menu.py - функции для работы с меню, для вывода информации от бота
#### Все остальное описано в программе

