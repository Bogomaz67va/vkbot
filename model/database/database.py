import sqlalchemy



class DataBase:
    def __init__(self, db):
        self.db = db
        self.engine = sqlalchemy.create_engine(self.db)
        self.connection = self.engine.connect()

    def insert_users(self, users_ids):
        self.connection.execute(f"INSERT INTO Users (id, users_id) VALUES (DEFAULT, {users_ids});")

    def select_users(self, event):
        result_dict = dict()
        result_db = self.connection.execute("select * from Users").fetchall()
        for item in result_db:
            result_dict[item[1]] = item[0]

        if result_dict.get(event.user_id):
            result = result_dict.get(event.user_id)
            return result
        else:
            self.insert_users(event.user_id)

    def select_users_lists(self, table_name):
        result_db = self.connection.execute(f"select * from {table_name}").fetchall()
        result = list()
        for item in result_db:
            result.append(item[1])
        return result

    def insert_users_like_list(self, users_like, id_users):
        self.connection.execute(
            f"INSERT INTO Userslikelist (id, users_like, id_users) VALUES (DEFAULT, {users_like}, {id_users})")

    def insert_users_black_list(self, users_black, id_users):
        self.connection.execute(
            f"INSERT INTO Usersblacklist (id, users_black, id_users) VALUES (DEFAULT, {users_black}, {id_users})")
