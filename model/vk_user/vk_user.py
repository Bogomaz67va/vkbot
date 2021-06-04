from vk_api.vk_api import VkApi
from model.settings.config import login, password


class VkUser(VkApi):
    """Класс для работы с правами доступа пользователь"""
    def sex_status(self):
        """возвращает противоположный пол"""
        result = {
            2: 1,
            1: 2,
        }
        return result

    def user_get(self, id_user: int):
        """Возвращает расширенную информацию о пользователях, имя и фамилия"""
        response = self.method('users.get', {'user_ids': id_user})
        result = f"{response[0]['first_name']} {response[0]['last_name']}"
        return result

    def photos_get(self, user_id):
        """Обработка и получение трех самых залайканных фото или закоменченных"""
        photos_get = self.method('photos.get', {'owner_id': user_id, 'album_id': 'profile', 'extended': 1})
        check_likes_comments = list()
        for item in photos_get['items']:
            photo = f"photo{item['owner_id']}_{item['id']}"
            result = [item['likes']['count'], item['comments']['count'], photo]
            check_likes_comments.append(result)
        if check_likes_comments:
            lst = sorted(check_likes_comments, key=lambda x: x[0] if x[0] != 0 else x[1], reverse=True)
            if len(lst) >= 3:
                result = [i[2] for i in lst[:3]]
                return result
            elif len(lst) < 3 and len(lst) != 0:
                result = [i[2] for i in lst]
                return result
            else:
                return 'что то пошло не так'

    def check_city(self, city: str):
        """Проверка на существование города, используя вк поиск"""
        check_city = self.method('users.search', {'hometown': city, 'count': 1})
        if check_city['items']:
            return True
        else:
            return False

    def search_users(self, home_town=None, age_from=16, age_to=55, sex_user=0, status_user=None):
        """Возвращает список пользователей в соответствии с заданным критерием поиска"""
        result = list()
        search = self.method("users.search",
                             {"hometown": home_town, "age_from": age_from, "age_to": age_to, "sex": sex_user,
                              "status": status_user, "count": 1000, "has_photo": 1, "sort": 1})
        for item_id in search['items']:
            if item_id['can_access_closed']:
                result.append(item_id['id'])
        return result


def vk_user():
    """Отправка экземпляра класса для дальнейшей работы"""
    user = VkUser(login=login, password=password)
    user.auth()
    return user
