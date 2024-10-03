from flask import Blueprint, request
from controllers.comment_controller import CommentController


comment_router = Blueprint('comment', __name__)
controller = CommentController()


@comment_router.post('/create')
def create_comment():
    json = request.get_json()
    return controller.create(json)