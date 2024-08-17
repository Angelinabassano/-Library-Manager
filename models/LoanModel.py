import psycopg2
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime
from config.Connection import Connection


class LoanModel:
    def __init__(self):
        self.db = Connection()


    def verify_data(self, book_id, user_id):

        query = "SELECT * FROM books WHERE book_id = %s AND user_id = %s"
        params = (book_id, user_id,)
        try:
            return self.db.execute_query(query, params)
        except Exception as e:
            return f"Error verifying data: {e}"

    def create_loan(self, loan_id, book_id, user_id, loan_date):

        query_loan = "INSERT INTO loans (loan_id, book_id, user_id, loan_date, return_date) VALUES (%s, %s, %s, %s, %s + INTERVAL '21 days')"

        params_loan = (loan_id, book_id, user_id, loan_date, loan_date)

        try:
            return self.db.update_query(query_loan, params_loan)
        except Exception as e:
            return f"Error when creating the book: {e}"


    def decrease_stock(self, book_id, stock):
        query = "UPDATE books SET stock = stock - %s WHERE book_id = %s AND stock > 0"
        params = (stock, book_id)

        try:
            return self.db.update_query(query, params)
        except Exception as e:
            return f"Error reducing stock: {e}"


    def final_loan(self, loan_id, final_date):

        query_update_final_date = "UPDATE loans SET final_date = %s WHERE loan_id = %s"
        params_update_final_date = (final_date, loan_id)

        query_get_book_id = "SELECT book_id FROM loans WHERE loan_id = %s"
        params_get_book_id = (loan_id,)

        query_update_stock = "UPDATE books SET stock = stock + 1 WHERE book_id = %s"


        try:
            self.db.update_query(query_update_final_date, params_update_final_date)

            result = self.db.execute_query(query_get_book_id, params_get_book_id)
            if result:
                book_id = result[0][0]
                params_update_stock = (book_id,)
                self.db.update_query(query_update_stock, params_update_stock)
            else:
                raise ValueError("Loan ID not found")

            return True

        except Exception as e:
            return f"Error updating final date and returning book: {e}"

    def increase_stock(self, book_id, stock):
        query = "UPDATE books SET stock = stock + 1 WHERE book_id = %s"
        params = (book_id, stock)

        try:
            return self.db.execute_query(query, params)
        except Exception as e:
            return f"Error increasing stock: {e}"

    def get_overdue_loans(self):
        query_overdue_loans = "SELECT loan_id, user_id, return_date, notification, last_notification_date FROM loans WHERE return_date < %s"
        params_overdue_loans = (datetime.now().date(),)

        try:
            overdue_loans = self.db.execute_query(query_overdue_loans, params_overdue_loans)
            return overdue_loans
        except Exception as e:
            return f"Error fetching overdue loans: {e}"

    def notify_overdue_loans(self):
        overdue_loans = self.get_overdue_loans()
        for loan in overdue_loans:
            loan_id, user_id, return_date, notification, last_notification_date = loan

            # Verificar si se necesita enviar una notificación
            now = datetime.now().date()
            if not notification or (last_notification_date and (now - last_notification_date).days >= 3):
                # Recuperar la dirección de correo electrónico del usuario
                query_get_email = "SELECT email FROM users WHERE user_id = %s"
                params_get_email = (user_id,)

                try:
                    result = self.db.execute_query(query_get_email, params_get_email)
                    if result:
                        user_email = result[0][0]
                        subject = "Book Return Overdue"
                        body = f"Dear User,\n\nYour book loan with ID {loan_id} is overdue. Please return the book as soon as possible.\n\nThank you."
                        self.send_email(user_email, subject, body)

                        # Actualizar la fecha de la última notificación y marcar el préstamo como notificado
                        self.update_last_notification_date(loan_id)
                        self.mark_loan_notified(loan_id)

                except Exception as e:
                    return f"Error fetching user email or sending notification: {e}"

    def update_last_notification_date(self, loan_id):
        query_update_last_notification = "UPDATE loans SET last_notification_date = %s WHERE loan_id = %s"
        params_update_last_notification = (datetime.now().date(), loan_id)

        try:
            self.db.execute_query(query_update_last_notification, params_update_last_notification)
        except Exception as e:
            return f"Error updating last notification date: {e}"

    def mark_loan_notified(self, loan_id):  # Marca un préstamo como notificado.
        query_mark_notified = "UPDATE loans SET notification = TRUE WHERE loan_id = %s"
        params_mark_notified = (loan_id,)

        try:
            self.db.execute_query(query_mark_notified, params_mark_notified)
        except Exception as e:
            return f"Error marking loan as notified: {e}"

    def send_email(self, to_email, subject, body):
        from_email = "your_email@example.com"
        password = "your_password"

        msg = MIMEMultipart()
        msg['From'] = from_email
        msg['To'] = to_email
        msg['Subject'] = subject

        msg.attach(MIMEText(body, 'plain'))

        try:
            with smtplib.SMTP('smtp.example.com', 587) as server:
                server.starttls()
                server.login(from_email, password)
                server.sendmail(from_email, to_email, msg.as_string())
            print(f"Email sent to {to_email}")
        except Exception as e:
            print(f"Error sending email: {e}")



    def delete_loan(self, loan_id):
        # Primero, recuperamos el ID del libro para poder aumentar el stock
        query_get_book_id = "SELECT book_id FROM loans WHERE loan_id = %s"
        params_get_book_id = (loan_id,)

        # Query para eliminar el préstamo
        query_delete_loan = "DELETE FROM loans WHERE loan_id = %s"
        params_delete_loan = (loan_id,)

        # Query para aumentar el stock del libro
        query_update_stock = "UPDATE books SET stock = stock + 1 WHERE book_id = %s"

        try:
            # Recuperar el ID del libro
            result = self.db.execute_query(query_get_book_id, params_get_book_id)
            if result:
                book_id = result[0][0]

                # Aumentar el stock
                self.db.update_query(query_update_stock, (book_id,))

                # Eliminar el préstamo
                self.db.update_query(query_delete_loan, params_delete_loan)
                return True
            else:
                return f"Loan ID {loan_id} not found"
        except Exception as e:
            return f"Error deleting loan: {e}"