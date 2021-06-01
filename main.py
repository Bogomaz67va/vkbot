from vk_api.longpoll import VkEventType
from model.vk_user.vk_user import vk_user
from model.keyboard.keyboard import button_bot, button_bot_status, button_bot_age
from model.settings.settings_bot import vk_session, longpoll, users_db
from model.vk_user.community_msg import write_msg
import re
PATTERNS_CITY = r'^\*[A-za-zА-я-а-я]+'



sex_status = {
    2: 1,
    1: 2,
}

while True:

    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW and event.to_me:
            user_id = users_db.select_users(event)
            extended_city = ""
            extended_age = ""
            extended_sex = ""
            extended_status = ""
            result = vk_session.method("messages.getById",
                                       {"message_ids": [event.message_id], 'extended': 1,
                                        "group_id": 204759084, "fields": "city, sex"})

            if result['profiles'][0].get('city'):
                city_users = result['profiles'][0]['city']['title']
            else:
                city_users = 'Москва'

            result_text = result['items'][0]['text']
            user_full_name = result['profiles'][0]['id']
            user_sex = result['profiles'][0]['sex']

            if result_text == 'Привет Vkinder' or result_text == 'Назад' or result_text == 'Начать' or \
                    result_text == 'Привет':
                write_msg(event.user_id, "Я бот который подберет тебе пару!")
                write_msg(event.user_id, "Давай начнем")
                write_msg(event.user_id, "Выбери нужный поиск",
                          keyboard=button_bot("Поиск по параметрам", "Быстрый поиск"))
            elif result_text == 'Поиск по параметрам':
                write_msg(event.user_id, "Введи *город, обязательно слитно")

            elif re.search(PATTERNS_CITY, result_text):
                extended_city = result_text
                write_msg(event.user_id, "Выбери возвраст",
                          keyboard=button_bot_age("18 - 20", "21 - 25", "26 - 30", "31 - 35", "36 - 55"))

            elif result_text == "18 - 20" or result_text == "21 - 25" or result_text == "26 - 30" or \
                    result_text == "31 - 35" or result_text == "36 - 55":
                extended_age = result_text
                write_msg(event.user_id, "Выбери пол", keyboard=button_bot("1-женщина", "2-мужчина"))

            elif result_text == "1-женщина" or result_text == "2-мужчина":
                extended_sex = result_text
                write_msg(event.user_id, "Выбери статус", keyboard=button_bot_status("1 — не женат/не замужем",
                                                                                     "5 — всё сложно",
                                                                                     "6 — в активном поиске",
                                                                                     "0 — не указано"))
            elif result_text == "1 — не женат/не замужем" or \
                    result_text == "5 — всё сложно" or result_text == "6 — в активном поиске" \
                    or result_text == "0 — не указано":
                extended_status = result_text
                write_msg(event.user_id, "Нажми на поиск", keyboard=button_bot("Поиск"))

            elif result_text == 'Быстрый поиск' or result_text == 'Не нравиться' or result_text == "Поиск" \
                    or result_text == "Нравиться" or result_text == "Еще":

                search = vk_user().search_users(city_users, 16, 55, sex_status.get(user_sex), 6)

                for like in users_db.select_users_lists("Userslikelist"):
                    if like in search:
                        search.remove(like)

                for black in users_db.select_users_lists("Usersblacklist"):
                    if black in search:
                        search.remove(black)

                for item_id in search:
                    if result_text == "Нравиться":
                        users_db.insert_users_like_list(item_id, user_id)
                        search.remove(item_id)
                        write_msg(event.user_id, "Ищем дальше??? Или хватит", keyboard=button_bot("Поиск", "Пока"))

                    if result_text == "Не нравиться":
                        users_db.insert_users_black_list(item_id, user_id)
                        search.remove(item_id)
                        write_msg(event.user_id, "еще", keyboard=button_bot("Еще"))

                    if result_text == "Быстрый поиск" or result_text == "Поиск" or result_text == "Еще":
                        write_msg(event.user_id, 'Что-то я нашел')
                        attachment = vk_user().photos_get(item_id)
                        write_msg(event.user_id, "Нравиться???", keyboard=button_bot("Нравиться", "Не нравиться"),
                                  attachment=','.join(attachment))
                        search_user_id = f"https://vk.com/id{item_id}"
                        write_msg(event.user_id, search_user_id)
                    break

            elif result_text == 'Пока':
                write_msg(event.user_id, "Пока")
                write_msg(event.user_id, "Однажды ты найдешь свою любовь, человек)")
            else:
                write_msg(event.user_id, 'Нажми на кнопку', keyboard=button_bot("Привет Vkinder"))
