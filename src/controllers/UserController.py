from models.UserModel import UsersModels


class UserController:

    def __init__(self):
        self.user_model = UsersModels()

    def create_user(self, first_name, last_name, email, phone_number, address):
        try:
            if self.user_model.verify_user(email):
                return dict(status_code=400,
                            response= 'user already exists',
                            result=[first_name, last_name, email, phone_number, address])
            self.user_model.create_user(first_name, last_name, email, phone_number, address)
            return dict(status_code=200,
                        response='The user was created successfully',
                        result=[first_name, last_name, email, phone_number, address])
        except Exception as e:
            return dict(status_code=500,
                        response=f'Error creating user: {e}')

    def edit_user(self, user_id, first_name, last_name, phone_number, address):
        try:
            if not self.user_model.get_user(user_id):
                return dict(status_code=404,
                            response='user not found')
            self.user_model.edit_user(user_id, first_name, last_name, phone_number, address)
            return dict(status_code=200, response='User updated successfully')
        except Exception as e:
            return dict(status_code=500,
                        response=f'Error updating user: {e}')
