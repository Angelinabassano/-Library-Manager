from config.Connection import Connection


class CategoryModel:

    def __init__(self):
        self.db = Connection()

    def verify_category(self, category_id, category_name):
        query = "SELECT * FROM categories WHERE category_id = %s AND category_name = %s"
        params = (category_id, category_name)
        try:
            return self.db.execute_query(query, params)
        except Exception as e:
            return f'Error verifying category: {e}'

    def create_category(self, category_id, category_name):
        query = "INSERT INTO categories(category_id, category_name) VALUES(%s, %s)"
        params = (category_id, category_name)
        try:
            return self.db.update_query(query, params)
        except Exception as e:
            return f'Error when creating the category: {e}'

    def get_category_by_id(self, category_id):
        query = "SELECT * FROM categories WHERE category_id = %s"
        params = (category_id,)
        try:
            return self.db.execute_query(query, params)
        except Exception as e:
            return f'Error finding category_id: {e}'

    def get_category_by_name(self, category_name):
        query = "SELECT * FROM categories WHERE category_name = %s"
        params = (category_name,)
        try:
            return self.db.execute_query(query, params)
        except Exception as e:
            return f'Error finding category_name: {e}'

    def update_category(self, category_id, category_name):
        query = 'UPDATE categories SET category_name = %s WHERE category_id = %s'
        params = (category_id, category_name,)
        try:
            return self.db.update_query(query, params)
        except Exception as e:
            return f'Error modifying category: {e}'

    def delete_category(self, category_id):
        query = "DELETE FROM categories WHERE category_id = %s"
        params = (category_id,)
        try:
            return self.db.update_query(query, params)
        except Exception as e:
            return f'Error deleting category: {e}'


