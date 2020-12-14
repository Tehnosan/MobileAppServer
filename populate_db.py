from tinydb import TinyDB

from domain.recipe import Recipe
from utilities import Utils

Utils.create()
repo = Utils.repo
repo.clear()

repo.addRecipe(Recipe("1", "Lava Cake", "10", "easy"))
repo.addRecipe(Recipe("2", "Pizza", "25", "medium"))
repo.addRecipe(Recipe("3", "Lasagna", "45", "hard"))