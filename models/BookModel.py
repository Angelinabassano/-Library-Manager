from config.Connection import Connection


class BookModel:

    def __init__(self):
        self.db = Connection()

    def verify_data(self, book_id, title, author, category_id):
        query = "SELECT * FROM books WHERE (book_id = %S, title = %S, author = %s, category_id = %s)"
        params = (book_id, title, author, category_id)
        try:
            return self.db.execute_query(query, params)
        except Exception as e:
            return f'Error verifying data: {e}'

    def create_book(self, title, author, category_id, stock):
        query = "INSERT INTO books(title, author, category_id, stock) VALUES(%s, %s, %s, %s)"
        params = (title, author, category_id, stock)
        try:
            return self.db.update_query(query, params)
        except Exception as e:
            return f'Error when creating the book: {e}'
