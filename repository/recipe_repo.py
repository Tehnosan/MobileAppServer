from tinydb import Query

from domain.recipe import Recipe


class RecipeRepo:
    def __init__(self, database):
        self.table = database.table("Recipes")
        self.database = database

    def returnRecipes(self, username, limit, page):
        recipe = Query()
        elements = self.table.search(recipe.username == username)

        recipes = []

        start = limit * (page - 1)
        end = min(len(elements), limit * page)
        for i in range(start, end):
            recipes.append(Recipe(**elements[i]))

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