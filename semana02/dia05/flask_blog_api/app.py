from flask import Flask
from db import db
from flask_cors import CORS
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from config import Config

from routes.auth_router import auth_router
from routes.user_router import user_router

app = Flask(__name__)
cors = CORS(app)

app.config.from_object(Config)

db.init_app(app)
migrate = Migrate(app, db)
jwt = JWTManager(app)

app.register_blueprint(user_router, url_prefix='/api/user')
app.register_blueprint(auth_router, url_prefix='/api/auth')


if __name__ == '__main__':
    app.run(debug=True)