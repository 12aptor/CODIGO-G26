from flask import Blueprint, request
from controllers.post_controller import PostController


post_router = Blueprint('post', __name__)
controller = PostController()


@post_router.post('/create')
def create_post():
    json = request.form.to_dict()
    image = request.files.get('image')
    return controller.create(json, image)