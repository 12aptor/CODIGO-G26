from models.user_model import UserModel
from schemas.user_schema import UserSchema
from pydantic import ValidationError
import bcrypt
from db import db


class UserController:
    def __init__(self):
        self.model = UserModel

    def create(self, json):
        try:
            # validated_user = UserSchema(**json)
            validated_user = UserSchema.model_validate(json, strict=True)

            user = self.model.query.filter_by(email=validated_user.email).first()

            if user:
                return {
                    'message': 'El usuario ya existe'
                }, 400
            
            validated_user.password = self.hash_password(validated_user.password)

            new_user = self.model(**validated_user.model_dump())

            db.session.add(new_user)
            db.session.commit()
            
            return {
                'message': 'Usuario creado correctamente',
                'data': new_user.to_dict()
            }, 201
        except ValidationError as e:
            return {
                'message': 'Error al validar el usuario',
                'error': e.errors()
            }, 400
        except Exception as e:
            return {
                'message': 'Error al crear el usuario',
                'error': str(e)
            }, 500

    def list(self):
        try:
            users = self.model.query.all()

            return {
                'message': 'Listado de usuarios',
                'data': [user.to_dict() for user in users]
            }, 200
        except Exception as e:
            return {
                'message': 'Error al obtener los usuarios',
                'error': str(e)
            }, 500

    def update(self, id, json):
        try:
            validated_user = UserSchema.model_validate(json, strict=True)

            user = self.model.query.get(id)

            if not user:
                return {
                    'message': 'El usuario no existe'
                }, 404
            
            user.name = validated_user.name
            user.email = validated_user.email
            user.password = self.hash_password(validated_user.password)
            user.status = validated_user.status

            db.session.commit()

            return {
                'message': 'Usuario actualizado correctamente',
                'data': user.to_dict()
            }, 200
        except ValidationError as e:
            return {
                'message': 'Error al validar el usuario',
                'error': e.errors()
            }, 400
        except Exception as e:
            db.session.rollback()
            return {
                'message': 'Error al actualizar el usuario',
                'error': str(e)
            }, 500

    def delete(self):
        pass

    def hash_password(self, password):
        pwd_bytes = password.encode('utf-8')
        pwd_hashed = bcrypt.hashpw(pwd_bytes, bcrypt.gensalt())
        return pwd_hashed.decode('utf-8')