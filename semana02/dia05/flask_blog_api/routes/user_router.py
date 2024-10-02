from flask import Blueprint, request
from controllers.user_controller import UserController
from flask_jwt_extended import jwt_required


user_router = Blueprint('user', __name__)
controller = UserController()


@user_router.post('/create')
@jwt_required()
def create_user():
    json = request.get_json()
    return controller.create(json)

@user_router.get('/list')
@jwt_required()
def list_users():
    return controller.list()

@user_router.put('/update/<int:id>')
@jwt_required()
def update_user(id):
    json = request.get_json()
    return controller.update(id, json)

@user_router.get('/get/<int:id>')
@jwt_required()
def get_user(id):
    return controller.get_by_id(id)

@user_router.delete('/delete/<int:id>')
@jwt_required()
def delete_user(id):
    return controller.delete(id)