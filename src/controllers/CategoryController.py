from models.CategoryModel import CategoryModel


class CategoryController:

    def __init__(self):
        self.category_model = CategoryModel()

    def verify_category(self, category_id, category_name):
        try:
            category = self.category_model.verify_category(category_id, category_name)
            if category:
                return {'status_code': 200, 'response': 'Verify category', 'result': category}
            else:
                return {'status_code': 404, 'response': 'Don’t Verify category'}
        except Exception as e:
            return {'status_code': 500, 'response': f'Error verifying category: {e}'}

    def create_category(self, category_id, category_name):
        try:
            self.category_model.create_category(category_id, category_name)
            return {
                'result': f'{category_id, category_name}'
            }
        except Exception as e:
            return {
                'status_code': 500,
                'response': f'Error when creating the category: {e}'
            }

    def get_category_by_id(self, category_id):
        try:
            category = self.category_model.get_category_by_id(category_id)
            if category:
                return {'status_code': 200, 'response': 'Category_id found', 'result': category}
            else:
                return {'status_code': 404, 'response': 'Category_id not found'}
        except Exception as e:
            return {'status_code': 500, 'response': f'Error finding category_id: {e}'}

    def get_category_by_name(self, category_name):
        try:
            category = self.category_model.get_category_by_name(category_name)
            if category:
                return {'status_code': 200, 'response': 'Category  found', 'result': category}
            else:
                return {'status_code': 404, 'response': 'Category not found'}
        except Exception as e:
            return {'status_code': 500, 'response': f'Error finding the category: {e}'}

    def update_category(self, category_id, category_name):
        try:
            print(f"Fetching category with category_id: {category_id}")
            category = self.get_category_by_id(category_id)

            if category['status_code'] == 404:
                return {'status_code': 404, 'response': "You cannot update a category that doesn't exist"}

            category_id = self.category_model.update_category(category_name, category_id)
            if category_id:
                return {'status_code': 200, 'response': 'Update completed successfully'}
            else:
                return {'status_code': 400, 'response': 'Update not done'}

        except Exception as e:
            return {
                'status_code': 500,
                'response': f'Error updating the category: {e}'
            }