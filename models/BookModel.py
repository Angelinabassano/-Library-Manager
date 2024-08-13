from config.Connection import Connection


class BookModel:

    def __init__(self):
        self.db = Connection()

    def verify_data(self, book_id, title, author, category_id):
        query = "SELECT * FROM books WHERE (book_id = %s, title = %s, author = %s, category_id = %s)"
        params = (book_id, title, author, category_id)
        try:
            return self.db.execute_query(query, params)
        except Exception as e:
            return f'Error verifying data: {e}'

    def create_book(self, book_id, title, author, category_id, stock):
        query = "INSERT INTO books(book_id, title, author, category_id, stock) VALUES(%s, %s, %s, %s, %s)"
        params = (category_id, title, author, category_id, stock)
        try:
            return self.db.update_query(query, params)
        except Exception as e:
            return f'Error when creating the book: {e}'

    def get_book_by_id(self, book_id):
        query = "SELECT * FROM books WHERE book_id = %s"
        params = (book_id,)
        try:
            return self.db.execute_query(query, params)
        except Exception as e:
            return f'Error finding book_id: {e}'

    def get_book_by_title(self, title):
        query = "SELECT * FROM books WHERE title = %s"
        params = (title,)
        try:
            return self.db.execute_query(query, params)
        except Exception as e:
            return f'Error finding the title of the Book: {e}'

    def get_book_by_author(self, author):
        query = "SELECT * FROM books WHERE (author = %s)"
        params = (author,)
        try:
            return self.db.execute_query(query, params)
        except Exception as e:
            return f'Error finding author of the Book: {e}'

    def update_book(self, book_id, title, author, category_id, stock):
        query = 'UPDATE books SET title = %s ,author = %s ,category_id = %s, stock = %s WHERE book_id = %s'
        params = (book_id, title, author, category_id, stock,)
        try:
            return self.db.update_query(query, params)
        except Exception as e:
            return f'Error updating book: {e}'

    def update_book_by_stock_increment(self, book_id, stock):
        query = "UPDATE books SET stock = stock + %s  WHERE book_id = %s"
        params = (stock, book_id,)
        try:
            return self.db.update_query(query, params)
        except Exception as e:
            return f'Error updating the stock of the book: {e}'

    def update_book_by_stock_decrease(self, book_id, stock):
        query = "UPDATE books SET stock = stock - %s WHERE book_id = %s"
        params = (stock, book_id,)
        try:
            return self.db.update_query(query, params)
        except Exception as e:
            return f'Error updating the stock of the book: {e}'

    def delete_book(self, book_id):
        query = "DELETE FROM books WHERE book_id = %s"
        params = (book_id,)
        try:
            return self.db.update_query(query, params)
        except Exception as e:
            return f'Error deleting book: {e}'