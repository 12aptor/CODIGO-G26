from flask import Blueprint, request
from controllers.auth_controller import AuthController


auth_router = Blueprint('auth', __name__)
controller = AuthController()


@auth_router.post('/login')
def login():
    json = request.get_json()
    return controller.login(json)

@auth_router.post('/register')
def register():
    json = request.get_json()
    return controller.register(json)

@auth_router.post('/refresh')
def refresh():
    json = request.get_json()
    return controller.refresh(json)