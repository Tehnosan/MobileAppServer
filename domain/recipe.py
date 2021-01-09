from flask import jsonify


class Recipe:
    def __init__(self, id, name, time, difficulty, photoName, latitude, longitude, *args, **kwargs):
        self.id = id
        self.name = name
        self.time = time
        self.difficulty = difficulty
        self.photoName = photoName
        self.latitude = latitude
        self.longitude = longitude
        self.username = ""

    def toDict(self):
        return {
            'id': self.id,
            'name': self.name,
            'time': self.time,
            'difficulty': self.difficulty,
            'photoName': self.photoName,
            'latitude': self.latitude,
            'longitude': self.longitude,
            'username' : self.username
        }

