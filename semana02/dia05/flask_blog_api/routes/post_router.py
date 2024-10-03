from flask import Blueprint, request
from controllers.post_controller import PostController
from flask_jwt_extended import jwt_required


post_router = Blueprint('post', __name__)
controller = PostController()


@post_router.post('/create')
@jwt_required()
def create_post():
    json = request.form.to_dict()
    image = request.files.get('image')
    return controller.create(json, image)

@post_router.get('/list')
def list_posts():
    return controller.list()

@post_router.get('/get/<int:id>')
def get_post(id):
    return controller.get_by_id(id)