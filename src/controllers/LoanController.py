from models.LoanModel import LoanModel
from models.BookModel import BookModel
from models.UserModel import UsersModels

class LoanController:
    def __init__(self):
        self.loan_model = LoanModel()
        self.book_model = BookModel()
        self.user_model = UsersModels()

    def verify_data(self, book_id, user_id):
        try:
            data = self.loan_model.verify_data(book_id, user_id)
            if data:
                return {'status_code': 200, 'response': 'Data verified', 'result': data}
            else:
                return {'status_code': 404, 'response': 'Data not verified'}
        except Exception as e:
            return {'status_code': 500, 'response': f'Error verifying data: {e}'}

    def create_loan(self, loan_id, book_id, user_id, loan_date):
        try:
            stock_result = self.loan_model.decrease_stock(book_id, 1)
            if not stock_result or stock_result < 1:
                return {'status_code': 409, 'response': 'No stock available'}

            loan_result = self.loan_model.create_loan(loan_id, book_id, user_id, loan_date)
            if loan_result > 0:
                return {'status_code': 200, 'response': 'Loan created successfully', 'result': loan_result}
            else:
                return {'status_code': 400, 'response': f'Loan creation failed: {loan_result}'}
        except Exception as e:
            return {'status_code': 500, 'response': f'Error creating loan: {e}'}

    def final_loan(self, loan_id, final_date):
        try:
            final_result = self.loan_model.final_loan(loan_id, final_date)
            if final_result is True:
                return {'status_code': 200, 'response': 'Loan finalized successfully'}
            else:
                return {'status_code': 400, 'response': f'Loan finalization failed: {final_result}'}
        except Exception as e:
            return {'status_code': 500, 'response': f'Error finalizing loan: {e}'}

    def get_overdue_loans(self):
        try:
            overdue_loans = self.loan_model.get_overdue_loans()
            if overdue_loans:
                return {'status_code': 200, 'response': 'Overdue loans found', 'result': overdue_loans}
            else:
                return {'status_code': 404, 'response': 'No overdue loans found'}
        except Exception as e:
            return {'status_code': 500, 'response': f'Error fetching overdue loans: {e}'}

    def notify_overdue_loans(self):
        try:
            notification_result = self.loan_model.notify_overdue_loans()
            if notification_result is None:
                return {'status_code': 200, 'response': 'Overdue loans notified'}
            else:
                return {'status_code': 400, 'response': f'Error notifying overdue loans: {notification_result}'}
        except Exception as e:
            return {'status_code': 500, 'response': f'Error notifying overdue loans: {e}'}

    def mark_loan_notified(self, loan_id):
        try:
            notification_result = self.loan_model.mark_loan_notified(loan_id)
            if "Error" not in notification_result:
                return {'status_code': 200, 'response': 'Loan marked as notified'}
            else:
                return {'status_code': 400, 'response': f'Failed to mark loan as notified: {notification_result}'}
        except Exception as e:
            return {'status_code': 500, 'response': f'Error marking loan as notified: {e}'}

    def update_last_notification_date(self, loan_id):
        try:
            update_result = self.loan_model.update_last_notification_date(loan_id)
            if "Error" not in update_result:
                return {'status_code': 200, 'response': 'Last notification date updated'}
            else:
                return {'status_code': 400, 'response': f'Failed to update last notification date: {update_result}'}
        except Exception as e:
            return {'status_code': 500, 'response': f'Error updating last notification date: {e}'}

    def delete_loan(self, loan_id):
        try:
            delete_result = self.loan_model.delete_loan(loan_id)
            if delete_result is True:
                return {'status_code': 200, 'response': 'Loan deleted successfully'}
            else:
                return {'status_code': 400, 'response': f'Failed to delete loan: {delete_result}'}
        except Exception as e:
            return {'status_code': 500, 'response': f'Error deleting loan: {e}'}