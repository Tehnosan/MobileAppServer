from tinydb import Query

from domain.recipe import Recipe


class Repo:
    def __init__(self, database):
        self.table = database.table("Recipes")
        self.database = database

    def returnRecipes(self):
        dictRecipes = self.table.all()
        recipes = []

        for recipe in dictRecipes:
            recipes.append(Recipe(**recipe))

        return recipes

    def addRecipe(self, recipe):
        self.table.insert(recipe.toDict())

    def returnOne(self, id):
        recipe = Query()
        element = self.table.search(recipe.id == id)

        if element:
            return Recipe(**element[0])

        return None

    def updateRecipe(self, recipe):
        recipeQuery = Query()
        self.table.update(recipe.toDict(), recipeQuery.id == recipe.id)

    def clear(self):
        self.database.drop_tables()