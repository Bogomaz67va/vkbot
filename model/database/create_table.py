import sqlalchemy


class CreateTable:
    def __init__(self, db):
        self.db = db
        self.engine = sqlalchemy.create_engine(self.db)
        self.connections = self.engine.connect()

    def create_table(self):
        """создание таблиц в БД"""
        self.connections.execute(
            "create table if not exists Users (id serial primary key, users_id integer unique not null);")
        self.connections.execute("create table if not exists UsersLikeList (id serial primary key, "
                                 "users_like integer unique not null, id_users integer not null references Users(id));")
        self.connections.execute("create table if not exists UsersBlackList (id serial primary key, "
                                 "users_black integer unique not null, "
                                 "id_users integer not null references Users(id));")
        self.connections.execute("create table if not exists AdvancedSearch ("
                                 "id serial primary key, "
                                 "city varchar(40) not null, "
                                 "age_from integer not null,"
                                 "age_to integer not null,"
                                 "user_sex integer not null,"
                                 "user_status integer not null,"
                                 "id_users integer not null references Users(id));")
        self.connections.close()
