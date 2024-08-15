from models.UserModel import UsersModels


class UserController:

    def __init__(self):
        self.user_model = UsersModels()

    def create_user(self, first_name, last_name, email, phone_number, address):
        try:
            if self.user_model.verify_user(email):
                return dict(status_code=400,
                            response= 'El usuario ya existe',
                            result=[first_name, last_name, email, phone_number, address])
            self.user_model.create_user(first_name, last_name, email, phone_number, address)
            return dict(status_code=200,
                        response='El usuario se creo de manera exitosa',
                        result=[first_name, last_name, email, phone_number, address])
        except Exception as e:
            return dict(status_code=500,
                        response=f'Error al crear el usuario: {e}')


