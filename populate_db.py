from domain.recipe import Recipe
from domain.user import User
from utilities.utilities import Utils

Utils.create()
recipe_repo = Utils.recipe_repo
user_repo = Utils.user_repo

recipe_repo.clear()

recipe_repo.addRecipe(Recipe("1", "Lava Cake", "10", "easy"))
recipe_repo.addRecipe(Recipe("2", "Pizza", "25", "medium"))
recipe_repo.addRecipe(Recipe("3", "Lasagna", "45", "hard"))

user_repo.addUser(User("admin", "pass"))
user_repo.addUser(User("Sandrino", "pass"))