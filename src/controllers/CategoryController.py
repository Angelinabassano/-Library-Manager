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
