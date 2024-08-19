from config.Connection import Connection


class UsersModels:

    def __init__(self):
        self.db = Connection()

    def verify_user(self, email):
        query = "SELECT * FROM users WHERE email = %s"
        params = (email,)
        try:
            result = self.db.execute_query(query, params)
            return result
        except Exception as e:
            print(f"Error verifying user: {e}")
            return None

    def create_user(self, user_id, first_name, last_name, email, phone_number, address):
        query = ("INSERT INTO users(user_id, first_name, last_name, email, phone_number, address) VALUES(%s, %s, %s, "
                 "%s, %s, %s)")
        params = (user_id, first_name, last_name, email, phone_number, address)
        try:
            return self.db.update_query(query, params)
        except Exception as e:
            print(f"Error creating user: {e}")
            return None

    def get_user(self, user_id):
        query = "SELECT * FROM users WHERE user_id = %s"
        params = (user_id,)
        try:
            return self.db.execute_query(query, params)
        except Exception as e:
            print(f"Error getting user: {e}")
            return None

    def update_user(self, user_id, first_name, last_name, phone_number, address):
        query = 'UPDATE users SET first_name = %s, last_name = %s, phone_number = %s, address = %s WHERE user_id = %s'
        params = (first_name, last_name, phone_number, address, user_id,)
        try:
            return self.db.update_query(query, params)
        except Exception as e:
            return f'Error updating user: {e}'

    def delete_user(self, user_id):
        query = "DELETE FROM users WHERE user_id = %s"
        params = (user_id,)
        try:
            return self.db.update_query(query, params)
        except Exception as e:
            print(f"Error deleting user: {e}")
            return None
