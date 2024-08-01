import psycopg2
from datetime import datetime, timedelta


class LoanModel:
    def __init__(self, connection):
        self.connection = connection

    def create_loan(self, book_id, user_id):    #Crea un préstamo y disminuye el stock del libro.
        try:
            cursor = self.connection.cursor()
            loan_date = datetime.now().date()
            return_date = loan_date + timedelta(days=21)
            final_date = None  # La fecha final se actualizará cuando se devuelva el libro

            cursor.execute(
                "INSERT INTO loans (book_id, user_id, loan_date, return_date, final_date) VALUES (%s, %s, %s, %s, %s)",
                (book_id, user_id, loan_date, return_date, final_date)
            )

            cursor.execute(
                "UPDATE books SET stock = stock - 1 WHERE book_id = %s AND stock > 0",
                (book_id,)
            )

            self.connection.commit()
            cursor.close()
            return True
        except Exception as e:
            print(f"Error creating loan: {e}")
            self.connection.rollback()
            return False

    def update_final_date(self, loan_id):  #Actualiza la fecha final cuando el libro es devuelto y aumenta el stock del libro.
        try:
            cursor = self.connection.cursor()

            final_date = datetime.now().date()

            cursor.execute(
                "UPDATE loans SET final_date = %s WHERE loan_id = %s",
                (final_date, loan_id)
            )

            cursor.execute("SELECT book_id FROM loans WHERE loan_id = %s", (loan_id,))
            result = cursor.fetchone()

            if result:
                book_id = result[0]

                cursor.execute(
                    "UPDATE books SET stock = stock + 1 WHERE book_id = %s",
                    (book_id,)
                )
            else:
                raise ValueError("Loan ID not found")

            self.connection.commit()
            cursor.close()
            return True
        except Exception as e:
            print(f"Error updating final date and returning book: {e}")
            self.connection.rollback()
            return False

    def get_overdue_loans(self):   #Obtiene los préstamos vencidos que aún no han sido notificados.
        try:
            cursor = self.connection.cursor()
            today = datetime.now().date()
            cursor.execute(
                "SELECT loan_id, user_id, return_date FROM loans WHERE return_date < %s AND notification = FALSE",
                (today,)
            )
            overdue_loans = cursor.fetchall()
            cursor.close()
            return overdue_loans
        except Exception as e:
            print(f"Error fetching overdue loans: {e}")
            return []

    def mark_loan_notified(self, loan_id):   #Actualiza last_notification_date al marcar el préstamo como notificado.
        try:
            cursor = self.connection.cursor()
            cursor.execute(
                "UPDATE loans SET notification = TRUE WHERE loan_id = %s",
                (loan_id,)
            )
            self.connection.commit()
            cursor.close()
        except Exception as e:
            print(f"Error marking loan as notified: {e}")
            self.connection.rollback()


def create_connection():
    try:
        connection = psycopg2.connect(
            dbname="",
            user="",
            password="",
            host="",
            port=""
        )
        return connection
    except Exception as e:
        print(f"Error connecting to the database: {e}")
        return None
