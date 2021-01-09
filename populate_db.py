from domain.recipe import Recipe
from domain.user import User
from utilities.utilities import Utils

Utils.create()
recipe_repo = Utils.recipe_repo
user_repo = Utils.user_repo

recipe_repo.clear()

images = ["1610112777026.jpeg", "1610112823546.jpeg", "1610112797294.jpeg"]

for i in range(3):
    recipe = Recipe(i.__str__(), "Name" + (i + 1).__str__(), "10", "easy", images[i], 46.56862409846464, 26.892768939521332)
    recipe.username = "a"
    recipe_repo.addRecipe(recipe)

user_repo.addUser(User("a", "a"))
user_repo.addUser(User("b", "b"))