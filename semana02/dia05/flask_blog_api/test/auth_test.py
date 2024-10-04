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

        register_json = {
            'name': 'Ana',
            'email': 'ana@gmail.com',
            'password': '123456',
            'status': True
        }
        register_response = client.post('/api/auth/register', json=register_json)
        assert register_response.status_code == 201
        assert register_response.json['message'] == 'Usuario creado correctamente'

        login_json = {
            'email': register_json['email'],
            'password': register_json['password']
        }
        login_response = client.post('/api/auth/login', json=login_json)
        assert login_response.status_code == 200

        access_token = login_response.json['data']['access_token']
        client.environ_base['HTTP_AUTHORIZATION'] = f'Bearer {access_token}'

        yield client
        db.session.remove()
        db.drop_all()


# def test_register(client: Flask):
#     json = {
#         "name": "Ana",
#         "email": "ana@gmail.com",
#         "password": "123456",
#         "status": True
#     }
#     response = client.post('/api/auth/register', json=json)
#     assert response.status_code == 201
#     assert response.json['message'] == 'Usuario creado correctamente'


def test_user_list(client: Flask):
    response = client.get('/api/user/list')
    assert response.status_code == 200
