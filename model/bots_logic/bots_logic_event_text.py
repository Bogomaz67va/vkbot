from model.keyboard.keyboard import button_bot, button_bot_status, button_bot_age
from model.vk_user.community_msg import write_msg
from model.vk_user.vk_user import vk_user


def user_greetings(event, user_full_name):
    write_msg(event.user_id, f"Привет {vk_user().user_get(user_full_name)}")
    write_msg(event.user_id, "Я бот который подберет тебе пару!")
    write_msg(event.user_id, "Перед тем как начать знай, что можно написать слово 'меню' или 'инфо',"
              "\nЧтобы посмотреть болле подробную информацию!")
    write_msg(event.user_id, "Давай начнем")
    write_msg(event.user_id, "Выбери нужный поиск", keyboard=button_bot("Поиск по параметрам", "Быстрый поиск"))


def enter_the_city_input(event):
    write_msg(event.user_id, "Введи город *город, обязательно слитно")


def enter_the_city_result(event, extended_city):
    if vk_user().check_city(extended_city):
        write_msg(event.user_id, "Выбери возвраст",
                  keyboard=button_bot_age("18 - 20", "21 - 25", "26 - 30", "31 - 35", "36 - 55"))
    else:
        write_msg(event.user_id, "Такого города не существует",
                  keyboard=button_bot("Поиск по параметрам", "Пока"))


def write_sex(event):
    write_msg(event.user_id, "Выбери пол", keyboard=button_bot("1-женщина", "2-мужчина"))


def write_status(event):
    write_msg(event.user_id, "Выбери статус", keyboard=button_bot_status("1 - не женат/не замужем",
                                                                         "5 - всё сложно",
                                                                         "6 - в активном поиске",
                                                                         "0 - не указано"))


def write_search(event):
    write_msg(event.user_id, "Нажми на поиск", keyboard=button_bot("Поиск"))


def logic_search(advanced_search, city_users, user_sex, users_db, result_text, user_id, event):
    if advanced_search:
        search = vk_user().search_users(advanced_search[1], advanced_search[2], advanced_search[3],
                                        advanced_search[4], advanced_search[5])
    else:
        search = vk_user().search_users(city_users, 18, 55, vk_user().sex_status().get(user_sex), 6)

    for like in users_db.select_users_lists("Userslikelist"):
        if like in search:
            search.remove(like)

    for black in users_db.select_users_lists("Usersblacklist"):
        if black in search:
            search.remove(black)
    if len(search) == 0:
        write_msg(event.user_id, "Больше некого нет", button_bot("Еще поищем!", "Пока"))

    for item_id in search:

        if result_text == "❤ Нравиться":
            users_db.insert_users_like_list(item_id, user_id)
            search.remove(item_id)
            write_msg(event.user_id, "Хороший выбор, продолжим?", keyboard=button_bot("Поиск", "Пока"))

        if result_text == "🖤 Не нравиться":
            users_db.insert_users_black_list(item_id, user_id)
            search.remove(item_id)
            write_msg(event.user_id, "Может еще?", keyboard=button_bot("Давай"))

        if result_text == "Быстрый поиск" or result_text == "Поиск" or result_text == "Давай":
            write_msg(event.user_id, 'Ох, дайка мне подумать...)')
            attachment = vk_user().photos_get(item_id)
            search_user_id = f"https://vk.com/id{item_id}"
            write_msg(event.user_id,
                      f"Нравиться???\n{search_user_id}\nЭто {vk_user().user_get(item_id)}\nВыбор за тобой",
                      keyboard=button_bot("❤ Нравиться", "🖤 Не нравиться", "Хватит"),
                      attachment=','.join(attachment))
        break
