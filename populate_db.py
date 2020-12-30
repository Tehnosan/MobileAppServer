from domain.recipe import Recipe
from domain.user import User
from utilities.utilities import Utils

Utils.create()
recipe_repo = Utils.recipe_repo
user_repo = Utils.user_repo

recipe_repo.clear()

for i in range(35):
    recipe = Recipe(i.__str__(), "Name" + (i + 1).__str__(), "10", "easy")
    recipe.username = "a"
    recipe_repo.addRecipe(recipe)

user_repo.addUser(User("a", "a"))
user_repo.addUser(User("b", "b"))