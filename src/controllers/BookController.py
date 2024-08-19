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
                return {'status_code': 404, 'response': 'Don´t Verify data'}
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

    def update_book(self, book_id, title, author, category_id, stock):
        try:
            print(f"Fetching book with book_id: {book_id}")
            book = self.get_book_by_id(book_id)

            if book['status_code'] == 404:
                return {'status_code': 404, 'response': "You cannot update a book that doesn't exist"}

            book_id = self.book_model.update_book(title, author, category_id, stock, book_id)
            if book_id:
                return {'status_code': 200, 'response': 'Update completed successfully'}
            else:
                return {'status_code': 400, 'response': 'Update not done'}

        except Exception as e:
            return {
                'status_code': 500,
                'response': f'Error updating the book: {e}'
            }

    def update_book_by_stock_increment(self, book_id, stock):
        try:
            result = self.book_model.update_book_by_stock_increment(stock, book_id, )
            return {
                'result': "Stock updated successfully"
            }
        except Exception as e:
            return {
                'status_code': 500,
                'response': f'Error updating book stock: {e}'
            }

    def update_book_by_stock_decrease(self, book_id, stock_decrement):
        if stock_decrement <= 0:
            return {
                'status_code': 400,
                'response': 'Stock decrement value must be positive'
            }
        try:
            self.book_model.update_book_by_stock_decrease(stock_decrement, book_id, )
            return {
                'status_code': 200,
                'response': 'Stock has been successfully decreased'
            }
        except Exception as e:
            return {
                'status_code': 500,
                'response': f'Error updating the stock of the book: {e}'
            }

    def delete_book(self, book_id, confirm):
        try:
            print(f"Fetching book with book_id: {book_id}")
            book = self.get_book_by_id(book_id)

            if book['status_code'] == 404:
                return book['You can not delete a book that doesn´t exists']

            if confirm:
                self.book_model.delete_book(book_id)
                return {'status_code': 200, 'response': 'The book was deleted'}
            else:
                return {'status_code': 400, 'response': 'Deletion not confirmed'}
        except Exception as e:
            print(f"Exception in delete_book: {e}")
            return {'status_code': 500, 'response': f'Error deleting book: {e}'}
