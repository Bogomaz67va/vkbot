import vk_api
from vk_api.longpoll import VkLongPoll


from model.database.create_table import CreateTable
from model.database.database import DataBase
from model.settings.config import db_bot, token

users_create = CreateTable(db=db_bot)
users_create.create_table()

vk_session = vk_api.VkApi(token=token)
longpoll = VkLongPoll(vk_session)
vk = vk_session.get_api()

users_db = DataBase(db=db_bot)