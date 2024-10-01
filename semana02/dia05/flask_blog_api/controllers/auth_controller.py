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

            if not user:
                return {
                    'message': 'El usuario no existe'
                }, 404
            
            

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