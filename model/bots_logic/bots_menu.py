from model.keyboard.keyboard import button_bot
from model.vk_user.community_msg import write_msg
from model.vk_user.vk_user import vk_user


def write_menu(event):
    write_msg(event.user_id, "Привет, ты попал в меню")
    write_msg(event.user_id, "Здесь ты можешь посмотреть людей в разных списках")
    write_msg(event.user_id, "Для этого нажми на кнопку",
              keyboard=button_bot("Избранный список", "Черный список", "Пока"))


def write_black_list(event, users_db, user_id):
    write_msg(event.user_id, 'Посмотри на последних 10 людей в черном списке')
    result_black = users_db.select_list('Usersblacklist', 'users_black', user_id)
    if result_black:
        for item in result_black:
            attachment = vk_user().photos_get(item)
            write_msg(event.user_id, f"https://vk.com/id{item}\n{vk_user().user_get(item)}",
                      attachment=','.join(attachment))
    else:
        write_msg(event.user_id, "У вас пока нет людей в черном списке", button_bot("меню"))
    write_msg(event.user_id, "Нажми на кнопку чтобы вернуться в меню", button_bot("меню"))


def write_like_list(event, users_db, user_id):
    write_msg(event.user_id, 'Посмотри на последних 10 людей в избранном списке')
    result_like = users_db.select_list('Userslikelist', 'users_like', user_id)
    if result_like:
        for item in result_like:
            attachment = vk_user().photos_get(item)
            write_msg(event.user_id, f"https://vk.com/id{item}\n{vk_user().user_get(item)}",
                      attachment=','.join(attachment))
    else:
        write_msg(event.user_id, "У вас пока нет людей в избранном списке", button_bot("меню"))
    write_msg(event.user_id, "Нажми на кнопку чтобы вернуться в меню", button_bot("меню"))
