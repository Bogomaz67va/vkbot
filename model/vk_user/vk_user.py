from vk_api.vk_api import VkApi
from model.settings.config import login, password


class VkUser(VkApi):

    def sex_status(self):
        result = {
            2: 1,
            1: 2,
        }
        return result

    def photos_get(self, user_id):
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
        check_city = self.method('users.search', {'hometown': city, 'count': 1})
        if check_city['items']:
            return True
        else:
            return False

    def search_users(self, home_town=None, age_from=16, age_to=55, sex_user=0, status_user=None):
        result = list()
        search = self.method("users.search",
                             {"hometown": home_town, "age_from": age_from, "age_to": age_to, "sex": sex_user,
                              "status": status_user, "count": 1000, "has_photo": 1, "sort": 1})
        for item_id in search['items']:
            if item_id['can_access_closed']:
                result.append(item_id['id'])
        return result


def vk_user():
    user = VkUser(login=login, password=password)
    user.auth()
    return user
