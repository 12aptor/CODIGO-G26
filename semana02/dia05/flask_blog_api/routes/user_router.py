from flask import Blueprint, request
from controllers.user_controller import UserController


user_router = Blueprint('user', __name__)
controller = UserController()

@user_router.post('/create')
def create_user():
    json = request.get_json()
    return controller.create(json)

@user_router.get('/list')
def list_users():
    return controller.list()

@user_router.put('/update/<int:id>')
def update_user(id):
    json = request.get_json()
    return controller.update(id, json)

@user_router.get('/get/<int:id>')
def get_user(id):
    return controller.get_by_id(id)

@user_router.delete('/delete/<int:id>')
def delete_user(id):
    return controller.delete(id)