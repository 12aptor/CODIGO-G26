from models.user_model import UserModel


class UserController:
    def __init__(self):
        self.model = UserModel

    def create(self):
        try:
            # Validar los datos

            return {
                'message': 'Usuario creado correctamente',
                'data': '-'
            }, 201
        except Exception as e:
            return {
                'message': 'Error al crear el usuario',
                'error': e.args[0]
            }, 500

    def list(self):
        pass

    def update(self):
        pass

    def delete(self):
        pass
