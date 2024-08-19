from config.Connection import Connection


class UsersModels:

    def __init__(self):
        self.db = Connection()

    def verify_user(self, email):
        try:
            query = "SELECT * FROM users WHERE email = %s"
            params = (email,)
            result = self.db.execute_query(query, params)
            return result
        except Exception as e:
            print(f"Error verifying user: {e}")
            return None

    def create_user(self, first_name, last_name, email, phone_number, address):  # aqui falta un try cath
        try:
           query = "INSERT INTO users(first_name, last_name, email, phone_number, address) VALUES(%s, %s, %s, %s, %s)"
           params = (first_name, last_name, email, phone_number, address)
           return self.db.update_query(query, params)
        except Exception as e:
            print(f"Error creating user: {e}")
            return None

    def get_user(self, user_id):
        try:
            query = "SELECT * FROM users WHERE user_id = %s"
            params = (user_id,)
            result = self.db.execute_query(query, params)
            return result
        except Exception as e:
            print(f"Error getting user: {e}")
            return None

    def edit_user(self, user_id, first_name, last_name, phone_number, address):
        try:
            updates = []
            params = []

            if first_name:
                updates.append("first_name = %s")
                params.append(first_name,)
            if last_name:
                updates.append("last_name = %s")
                params.append(last_name,)
            if phone_number:
                updates.append("phone_number = %s")
                params.append(phone_number,)
            if address:
                updates.append("address = %s")
                params.append(address,)

            if not updates:
                return True

            query = f"UPDATE users SET {', '.join(updates)} WHERE user_id = %s"
            params.append(user_id)

            return self.db.update_query(query, params)

        except Exception as e:
            print(f"Error editing user: {e}")
            return False

    def delete_user(self, user_id):
        try:
            query = "DELETE FROM users WHERE user_id = %s"
            params = (user_id,)
            return self.db.update_query(query, params)
        except Exception as e:
            print(f"Error deleting user: {e}")
            return None









