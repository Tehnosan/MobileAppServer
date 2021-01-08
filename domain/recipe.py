from flask import jsonify


class Recipe:
    def __init__(self, id, name, time, difficulty, photoName, *args, **kwargs):
        self.id = id
        self.name = name
        self.time = time
        self.difficulty = difficulty
        self.photoName = photoName
        self.username = ""

    def toDict(self):
        return {
            'id': self.id,
            'name': self.name,
            'time': self.time,
            'difficulty': self.difficulty,
            'photoName': self.photoName,
            'username' : self.username
        }

