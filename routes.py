from sanic import Blueprint
from sanic.response import json
from models import User

blueprint = Blueprint("users")

users = {}

@blueprint.route("/users", methods=["GET"])
async def get_users(request):
    return json({"users": list(users.values())})

@blueprint.route("/users/<user_id:int>", methods=["GET"])
async def get_user(request, user_id):
    user = users.get(user_id)
    if user:
        return json(user)
    return json({"error": "User not found"}, status=404)

@blueprint.route("/users", methods=["POST"])
async def create_user(request):
    data = request.json
    user = User(**data)
    users[user.id] = user.to_dict()
    return json(user.to_dict(), status=201)

@blueprint.route("/users/<user_id:int>", methods=["PUT"])
async def update_user(request, user_id):
    if user_id not in users:
        return json({"error": "User not found"}, status=404)
    users[user_id].update(request.json)
    return json(users[user_id])

@blueprint.route("/users/<user_id:int>", methods=["DELETE"])
async def delete_user(request, user_id):
    if user_id in users:
        del users[user_id]
        return json({"message": "User deleted"})
    return json({"error": "User not found"}, status=404)
