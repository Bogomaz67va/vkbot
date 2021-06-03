from vk_api.longpoll import VkEventType
from model.keyboard.keyboard import button_bot
from model.settings.settings_bot import vk_session, longpoll, users_db
from model.vk_user.community_msg import write_msg
from model.vk_user.regular_expression import regular_search, PATTERNS_CITY
from model.bots_logic.bots_logic_event_text import user_greetings, enter_the_city_input, \
    enter_the_city_result, write_sex, write_status, write_search, logic_search
from model.bots_logic.bots_menu import write_menu, write_like_list, write_black_list


def main():
    while True:
        extended_city = ""
        extended_age = ""
        extended_sex = ""
        extended_status = ""

        for event in longpoll.listen():
            if event.type == VkEventType.MESSAGE_NEW and event.to_me:
                user_id = users_db.select_users(event)

                if len(extended_city) != 0 and len(extended_age) != 0 and len(extended_sex) != 0 and len(
                        extended_status) != 0:
                    users_db.insert_advanced_search(extended_city, int(extended_age[0]),
                                                    int(extended_age[1]),
                                                    int(extended_sex[0]), int(extended_status[0]),
                                                    user_id)

                advanced_search = users_db.select_advanced_search(user_id)

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
                    user_greetings(event, user_full_name)

                elif result_text == 'Поиск по параметрам':
                    enter_the_city_input(event)

                elif regular_search(PATTERNS_CITY, result_text):
                    extended_city = result_text.replace('*', '')
                    enter_the_city_result(event, extended_city)

                elif result_text == "18 - 20" or result_text == "21 - 25" or result_text == "26 - 30" or \
                        result_text == "31 - 35" or result_text == "36 - 55":
                    extended_age = result_text.split(' - ')
                    write_sex(event)

                elif result_text == "1-женщина" or result_text == "2-мужчина":
                    extended_sex = result_text.split('-')
                    write_status(event)
                elif result_text == "1 - не женат/не замужем" or \
                        result_text == "5 - всё сложно" or result_text == "6 - в активном поиске" \
                        or result_text == "0 - не указано":
                    extended_status = result_text.split(' - ')
                    write_search(event)

                elif result_text == 'Быстрый поиск' or result_text == 'Не нравиться' or result_text == "Поиск" \
                        or result_text == "Нравиться" or result_text == "Давай":
                    logic_search(advanced_search, city_users, user_sex, users_db, result_text, user_id, event)
                elif result_text == "меню" or result_text == "Меню":
                    write_menu(event)
                elif result_text == "Черный список":
                    write_black_list(event, users_db, user_id)
                elif result_text == "Избранный список":
                    write_like_list(event, users_db, user_id)
                elif result_text == 'Пока' or result_text == 'Хватит':
                    write_msg(event.user_id, "Пока")
                    users_db.delete_advanced_search(user_id)
                    extended_city = ""
                    extended_age = ""
                    extended_sex = ""
                    extended_status = ""
                    write_msg(event.user_id, "Однажды ты найдешь свою любовь, человек)\nА если не получиться пиши",
                              button_bot("Привет Vkinder"))
                else:
                    write_msg(event.user_id, 'Нажми на кнопку', keyboard=button_bot("Привет Vkinder"))
