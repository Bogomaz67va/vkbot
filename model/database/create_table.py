import sqlalchemy



class CreateTable:
    def __init__(self, db):
        self.db = db
        self.engine = sqlalchemy.create_engine(self.db)
        self.connections = self.engine.connect()

    def create_table(self):
        self.connections.execute(
            "create table if not exists Users (id serial primary key, users_id integer unique not null);")
        self.connections.execute("create table if not exists UsersLikeList (id serial primary key, "
                                 "users_like integer unique not null, id_users integer not null references Users(id));")
        self.connections.execute("create table if not exists UsersBlackList (id serial primary key, "
                                 "users_black integer unique not null, "
                                 "id_users integer not null references Users(id));")
        self.connections.close()
