from models.UserModel import UsersModels


class UserController:

    def __init__(self):
        self.user_model = UsersModels()

    def create_user(self, user_id, first_name, last_name, email, phone_number, address):
        try:
            if self.user_model.verify_user(email):
                return dict(status_code=400,
                            response= 'User already exists',
                            result=[user_id, first_name, last_name, email, phone_number, address])
            self.user_model.create_user(user_id, first_name, last_name, email, phone_number, address)
            return dict(status_code=200,
                        response='User create successfully',
                        result=[user_id, first_name, last_name, email, phone_number, address])
        except Exception as e:
            return dict(status_code=500,
                        response=f'Error creating user: {e}')

    def get_user(self, user_id):
        try:
            user = self.user_model.get_user(user_id)
            if user:
                return {'status_code': 200, 'response': 'user_id found', 'result': user}
            else:
                return {'status_code': 404, 'response': 'user_id not found'}
        except Exception as e:
            return {'status_code': 500, 'response': f'Error finding user_id: {e}'}

    def update_user(self, user_id, first_name, last_name, phone_number, address):
        try:
            if not self.user_model.get_user(user_id):
                return dict(status_code=404,
                            response='User not found')
            self.user_model.update_user(user_id, first_name, last_name, phone_number, address)
            return dict(status_code=200, response='User updated successfully')
        except Exception as e:
            return dict(status_code=500,
                        response=f'Error updating user: {e}')

    def delete_user(self, user_id):
        try:
            if not self.user_model.get_user(user_id):
                return dict(status_code=404,
                            response='User not found')
            self.user_model.delete_user(user_id)
            return dict(status_code=200,
                        response='User successfully deleted')
        except Exception as e:
            return dict(status_code=500, response=f'Error deleting user: {e}')