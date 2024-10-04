import pytest
from app import app, db
from flask import Flask


@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    
    with app.app_context():
        client = app.test_client()
        db.create_all()
        yield client
        db.session.remove()
        db.drop_all()


def test_register(client: Flask):
    json = {
        "name": "Ana",
        "email": "ana@gmail.com",
        "password": "123456",
        "status": True
    }
    response = client.post('/api/auth/register', json=json)
    print(response.json)
    assert response.status_code == 201
