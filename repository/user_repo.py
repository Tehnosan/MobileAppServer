from tinydb import Query

from domain.user import User


class UserRepo:
    def __init__(self, database):
        self.table = database.table("Users")

    def addUser(self, user):
        self.table.insert(user.toDict())

    def returnOne(self, username, password):
        user = Query()
        element = self.table.search(user.username == username and user.password == password)

        if element:
            return User(**element[0])

        return None