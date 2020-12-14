class User:
    def __init__(self, username, password, *args, **kwargs):
        self.username = username
        self.password = password

    def toDict(self):
        return {
            'username': self.username,
            'password': self.password
        }