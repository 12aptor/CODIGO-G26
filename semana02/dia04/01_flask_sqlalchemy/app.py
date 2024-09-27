from flask import Flask
from db import db
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql://postgres:root@localhost:5432/flask_sqlalchemy'

db.init_app(app)

class UserModel(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    email: Mapped[str] = mapped_column(String(200))

@app.get("/")
def index():
    return 'Hola Flask 😀'

if __name__ == '__main__':
    app.run(debug=True)