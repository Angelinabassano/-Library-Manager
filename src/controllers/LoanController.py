from models.LoanModel import LoanModel
from models.BookModel import BookModel

class LoanController:
    def __init__(self):
        self.loan_model = LoanModel()
    def verify_data(self,book_id):
        try:
            stock = self.book_model.verify_data(book_id)
            if stock:
                return {'status_code': 200, 'response': 'stock available', 'result': stock}

            else:
                return {'status_code': 409, 'response': 'No stock available'}

        except Exception as e:
            return {'status_code': 500, 'response': f'Error verify data: {e}'}

    def create_loan(self, book_id, user_id, loan_date):
        try:
            self.loan_model.create_loan(book_id, user_id, loan_date)
            return {
                'result': f'{book_id, user_id, loan_date, loan_date}'
            }
        except Exception as e:
            return {'status_code': 500, 'response': f'Error creating loan: {e}'}

    def decrease_stock(self, book_id, stock):
        try:
            decrease = self.book_model.create_loan(book_id, stock)
            if decrease:
                return {'status_code': 200, 'response': 'stock decrease', 'result': decrease}

        except Exception as e:
            return {'status_code': 500, 'response': f'Error decreasing stock: {e}'}


    def send_email(self, email, subject, body):
        try:
            email = self.user_model.create.user(email)
            if email:
                return {'status_code': 200, 'response': 'Email sent', 'result': email}

            else:
                return {'status_code': 409, 'response': 'email not sent'}
        except Exception as e:
            return {'status_code': 500, 'response': f'Error sending email : {e}'}


    def mark_loan_notified(self, loan_id, notification):
        try:
            notified = self.loan_model.mark_loan_notified(loan_id, notification)
            if notification:
                return {'status_code': 200, 'response': 'Notification True', 'result': notified}

            else:
                return {'status_code': 409, 'response': 'Notification False'}
        except Exception as e:
            return {'status_code': 500, 'response': f'Error Notification : {e}'}


    def get_overdue_loans(self, loan_id):
        try:
            overdue = self.loan_model.get_overdue_loans(loan_id,)
            if overdue:
                return {'status_code': 200, 'response': 'Book overdue', 'result': overdue}

            else:
                return {'status_code': 409, 'response': 'Book no overdue'}

        except Exception as e:
            return {'status_code': 500, 'response': f'Error overdue : {e}'}

    def notify_overdue_loans(self, loan_id, book_id):
        try:
            overdue = self.loan_model.get_overdue_loans(loan_id, book_id)
            if overdue:
                return {'status_code': 200, 'response': 'Book overdue', 'result': overdue}

            else:
                return {'status_code': 409, 'response': 'Book no overdue'}
        except Exception as e:
            return {'status_code': 500, 'response': f'Error notifying overdue : {e}'}
    def update_last_notification_date(self, loan_id):
        try:
            email = self.loan_model.get_overdue_loans(loan_id)
            if email:
                return {'status_code': 200, 'response': 'Email sent', 'result': email}

            else:
                return {'status_code': 409, 'response': 'email not sent'}
        except Exception as e:
            return {'status_code': 500, 'response': f'Error in the last notification : {e}'}



    def final_loan(self, loan_id):
        try:
            final = self.loan_model.get_overdue_loans(loan_id)
            if final:
                return {'status_code': 200, 'response': 'Book delivered', 'result': final}

            else:
                return {'status_code': 409, 'response': 'Book overdue'}
        except Exception as e:
            return {'status_code': 500, 'response': f'Error final loan: {e}'}

    def increase_stock(self, book_id, stock):
        try:
            increase = self.book_model.create_loan(book_id, stock)
            if increase:
                return {'status_code': 200, 'response': 'stock increase', 'result': increase}

        except Exception as e:
            return {'status_code': 500, 'response': f'Error increasing stock: {e}'}