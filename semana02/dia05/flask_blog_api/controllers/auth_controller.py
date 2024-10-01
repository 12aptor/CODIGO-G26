from models.user_model import UserModel
from pydantic import ValidationError
from schemas.user_schema import LoginSchema
import bcrypt


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
                    'access_token': '',
                    'refresh_token': ''
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