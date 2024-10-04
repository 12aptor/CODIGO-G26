from flask import Flask
from db import db
from flask_cors import CORS
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from config import Config

from routes.auth_router import auth_router
from routes.user_router import user_router
from routes.post_router import post_router
from routes.comment_router import comment_router


app = Flask(__name__)
cors = CORS(app)

app.config.from_object(Config)

db.init_app(app)
migrate = Migrate(app, db)
jwt = JWTManager(app)

@jwt.unauthorized_loader
def custom_unauthorized_response(callback):
    return {
        'message': 'Credenciales incorrectas',
    }, 401

app.register_blueprint(user_router, url_prefix='/api/user')
app.register_blueprint(auth_router, url_prefix='/api/auth')
app.register_blueprint(post_router, url_prefix='/api/post')
app.register_blueprint(comment_router, url_prefix='/api/comment')


if __name__ == '__main__':
    app.run(debug=True)