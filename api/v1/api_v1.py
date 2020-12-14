from flask import Blueprint, jsonify, request

from utilities import Utils
from domain.recipe import Recipe


api = Blueprint('api_v1', __name__)

@api.route('/recipes')
def products():
    repo = Utils.repo
    list = repo.returnRecipes()
    result = []

    for element in list:
        result.append(element.toDict())

    return jsonify(result)

@api.route('/recipes/<id>')
def findOne(id):
    repo = Utils.repo
    recipe = repo.returnOne(int(id))

    return jsonify(recipe.toDict())

@api.route('/recipe', methods=['POST'])
def create():
    data = request.get_json()

    repo = Utils.repo
    repo.addRecipe(Recipe(**data))

    print("Post")
    print(data)

    return data

@api.route('/recipe/<id>', methods=['PUT'])
def update(id):
    data = request.get_json()

    repo = Utils.repo

    # if repo.returnOne(data["id"]):
    #     repo.updateRecipe(Recipe(**data))
    # else:
    #     repo.addRecipe(Recipe(**data))

    repo.updateRecipe(Recipe(**data))

    print("Put")
    print(data)

    return data


