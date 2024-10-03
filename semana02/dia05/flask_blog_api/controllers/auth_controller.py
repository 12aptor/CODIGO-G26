from models.user_model import UserModel
from pydantic import ValidationError
from schemas.user_schema import (
    LoginSchema,
    RefreshSchema,
    UserSchema
)
import bcrypt
from flask_jwt_extended import (
    create_access_token,
    create_refresh_token,
    decode_token
)
from db import db


class AuthController:
    def __init__(self):
        self.model = UserModel

    def login(self, json):
        try:
            validated_user = LoginSchema.model_validate(json, strict=True)

            user = self.model.query.filter_by(email=validated_user.email).first()

            if not user or user.status == False:
                return {
                    'message': 'Credenciales incorrectas'
                }, 401
            
            is_pwd_valid = bcrypt.checkpw(
                validated_user.password.encode('utf-8'),
                user.password.encode('utf-8')
            )
            
            if not is_pwd_valid:
                return {
                    'message': 'Credenciales incorrectas'
                }, 401
            
            return {
                'message': 'Usuario autenticado correctamente',
                'data': {
                    'access_token': create_access_token(identity=user.id),
                    'refresh_token': create_refresh_token(identity=user.id)
                }
            }, 200
        except ValidationError as e:
            return {
                'message': 'Error al validar las credenciales',
                'error': e.errors()
            }, 400
        except Exception as e:
            return {
                'message': 'Error al iniciar sesión',
                'error': str(e)
            }, 500
        
    def register(self, json):
        try:
            validated_user = UserSchema.model_validate(json, strict=True)

            user = self.model.query.filter_by(email=validated_user.email).first()

            if user:
                return {
                    'message': 'El usuario ya existe'
                }, 400
            
            validated_user.password = self.__hash_password(validated_user.password)

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
        
    def refresh(self, json):
        try:
            validated_token = RefreshSchema.model_validate(json, strict=True)

            dict_token = decode_token(validated_token.refresh_token)

            if dict_token['type'] != 'refresh':
                return {
                    'message': 'Error al actualizar las credenciales'
                }, 401

            return {
                'message': 'Token actualizado correctamente',
                'data': {
                    'access_token': create_access_token(identity=dict_token['sub'])
                }
            }, 200
        except ValidationError as e:
            return {
                'message': 'Error al validar las credenciales',
                'error': e.errors()
            }, 400
        except Exception as e:
            return {
                'message': 'Error al actualizar las credenciales',
                'error': str(e)
            }, 500
        
    def __hash_password(self, password):
        pwd_bytes = password.encode('utf-8')
        pwd_hashed = bcrypt.hashpw(pwd_bytes, bcrypt.gensalt())
        return pwd_hashed.decode('utf-8')