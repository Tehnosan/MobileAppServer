from flask import Blueprint, jsonify, request, json

from domain.user import User
from utilities.utilities import Utils
from domain.recipe import Recipe
from utilities.token import createToken, verify
from api.v1.sockets import socketio


api = Blueprint('api_v1', __name__)

class InvalidUsage(Exception):
    status_code = 400

    def __init__(self, message, status_code=None, payload=None):
        Exception.__init__(self)
        self.message = message
        if status_code is not None:
            self.status_code = status_code
        self.payload = payload

    def to_dict(self):
        rv = dict(self.payload or ())
        rv['message'] = self.message
        return rv

def getUsername():
    token = request.headers['Authorization'].split(" ")[1]

    credentials = verify(token)
    credentials = json.loads(credentials)

    return credentials["username"]

@api.errorhandler(InvalidUsage)
def handle_invalid_usage(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response

@api.route('/recipes/<limit>/<page>')
def products(limit, page):
    username = getUsername()

    recipe_repo = Utils.recipe_repo
    list = recipe_repo.returnRecipes(username, int(limit), int(page))
    result = []

    for element in list:
        result.append(element.toDict())

    return jsonify(result)

@api.route('/recipes/<id>')
def findOne(id):
    recipe_repo = Utils.recipe_repo
    recipe = recipe_repo.returnOne(int(id))

    return jsonify(recipe.toDict())

@api.route('/recipe', methods=['POST'])
def create():
    data = request.get_json()

    recipe_repo = Utils.recipe_repo

    recipe = Recipe(**data)
    recipe.username = getUsername()
    recipe.id = recipe_repo.length().__str__()

    recipe_repo.addRecipe(recipe)

    socketio.emit('recipe_added', data)

    print("Post")
    print(data)

    return data

@api.route('/recipe/<id>', methods=['PUT'])
def update(id):
    data = request.get_json()

    recipe_repo = Utils.recipe_repo

    recipe = Recipe(**data)
    recipe.username = getUsername()

    recipe_repo.updateRecipe(recipe)

    print("Put")
    print(data)

    return data

@api.route('/login', methods=['POST'])
def login():
    credentials = request.get_json()
    print(credentials)

    user_repo = Utils.user_repo
    user = User(**credentials)

    if user_repo.returnOne(user.username, user.password):
        return { 'token' : createToken(credentials)}
    else:
        raise InvalidUsage('Username or Password incorrect', status_code=410)
























