from tinydb import TinyDB
from repository.repo import *

class Utils:
    repo = None
    db = None

    @classmethod
    def create(cls):
        cls.db = TinyDB('./data/db.json')
        cls.repo = Repo(cls.db)