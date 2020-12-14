from tinydb import TinyDB
from repository.recipe_repo import *
from repository.user_repo import *


class Utils:
    recipe_repo = None
    user_repo = None
    db = None

    @classmethod
    def create(cls):
        cls.db = TinyDB('./data/db.json')
        cls.recipe_repo = RecipeRepo(cls.db)
        cls.user_repo = UserRepo(cls.db)