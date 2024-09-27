from flask import Flask
from db import db
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql://postgres:root@localhost:5432/flask_sqlalchemy'

db.init_app(app)

class UserModel(db.Model):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    email: Mapped[str] = mapped_column(String(200), unique=True)

with app.app_context():
    db.create_all()

@app.get("/")
def index():
    return 'Hola Flask 😀'

@app.post("/user/create")
def createUser():
    try:
        json = {
            'name': 'Pepito',
            'email': 'pepito@gmail.com'
        }
        user = UserModel(
            name=json['name'],
            email=json['email']
        )

        db.session.add(user)
        db.session.commit()

        return {
            'message': 'User created successfully',
            'data': {
                'id': user.id,
                'name': user.name,
                'email': user.email
            }
        }, 201
    except Exception as e:
        db.session.rollback()
        return {
            'message': 'Error to create user',
            'error': str(e)
        }

if __name__ == '__main__':
    app.run(debug=True)