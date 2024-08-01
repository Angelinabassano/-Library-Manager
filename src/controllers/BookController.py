from models.BookModel import BookModel


class BookController:

    def __init__(self):
        self.book_model = BookModel()

    def verify_data(self, book_id, title, author, category_id):
        try:
            book = self.book_model.verify_data(book_id, title, author, category_id)
            if book:
                return {'status_code': 200, 'response': 'Verify data', 'result': book}
            else:
                return {'status_code': 404, 'response': 'Don’t Verify data'}
        except Exception as e:
            return {'status_code': 500, 'response': f'Error verifying data: {e}'}

    def create_book(self, book_id, title, author, category_id, stock):
        try:
            self.book_model.create_book(book_id, title, author, category_id, stock)
            return {
                'result': f'{book_id, title, author, category_id, stock}'
            }
        except Exception as e:
            return {
                'status_code': 500,
                'response': f'Error when creating the book: {e}'
            }

    def get_book_by_id(self, book_id):
        try:
            book = self.book_model.get_book_by_id(book_id)
            if book:
                return {'status_code': 200, 'response': 'Book_id found', 'result': book}
            else:
                return {'status_code': 404, 'response': 'Book_id not found'}
        except Exception as e:
            return {'status_code': 500, 'response': f'Error finding book_id: {e}'}

    def get_book_by_title(self, title):
        try:
            book = self.book_model.get_book_by_title(title)
            if book:
                return {'status_code': 200, 'response': 'Book  found', 'result': book}
            else:
                return {'status_code': 404, 'response': 'Book not found'}
        except Exception as e:
            return {'status_code': 500, 'response': f'Error finding the title of the Book: {e}'}

    def get_book_by_author(self, author):
        try:
            book = self.book_model.get_book_by_author(author)
            if book:
                return {'status_code': 200, 'response': 'Book found', 'result': book}
            else:
                return {'status_code': 404, 'response': 'Book not found'}
        except Exception as e:
            return {'status_code': 500, 'response': f'Error finding author of the Book: {e}'}
