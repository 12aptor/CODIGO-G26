from flask import Flask
from db import db
from flask_cors import CORS
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from config import Config

app = Flask(__name__)
cors = CORS(app)

app.config.from_object(Config)

db.init_app(app)
migrate = Migrate(app, db)
jwt = JWTManager(app)

@app.get('/')
def index():
    return 'Hola Flask 😀'

if __name__ == '__main__':
    app.run(debug=True)