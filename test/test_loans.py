import pytest
from unittest.mock import MagicMock
from src.controllers.LoanController import LoanController


def test_verify_data_success(mocker):
    mock_loan_model = mocker.patch('src.controllers.LoanController.LoanModel')
    mock_loan_model_instance = mock_loan_model.return_value
    mock_loan_model_instance.verify_data.return_value = {'book_id': 'Book Test', 'user_id': 'User Test'}

    loan_controller = LoanController()
    book_id = "Book Test"
    user_id = "User Test"

    response = loan_controller.verify_data(book_id, user_id)

    assert response == {
        'status_code': 200,
        'response': 'Data verified',
        'result': {'book_id': 'Book Test', 'user_id': 'User Test'}
    }

    mock_loan_model_instance.verify_data.assert_called_once_with(book_id, user_id)


def test_verify_data_not_found(mocker):
    mock_loan_model = mocker.patch('src.controllers.LoanController.LoanModel')
    mock_loan_model_instance = mock_loan_model.return_value
    mock_loan_model_instance.verify_data.return_value = None

    loan_controller = LoanController()
    book_id = "Book Test"
    user_id = "User Test"

    response = loan_controller.verify_data(book_id, user_id)

    assert response == {
        'status_code': 404,
        'response': 'Data not verified'
    }

    mock_loan_model_instance.verify_data.assert_called_once_with(book_id, user_id)


def test_verify_data_exception(mocker):
    mock_loan_model = mocker.patch('src.controllers.LoanController.LoanModel')
    mock_loan_model_instance = mock_loan_model.return_value
    mock_loan_model_instance.verify_data.side_effect = Exception("Mocked exception")

    loan_controller = LoanController()
    book_id = "Book Test"
    user_id = "User Test"

    response = loan_controller.verify_data(book_id, user_id)

    assert response == {
        'status_code': 500,
        'response': 'Error verifying data: Mocked exception'
    }

    mock_loan_model_instance.verify_data.assert_called_once_with(book_id, user_id)


def test_create_loan_success(mocker):
    mock_loan_model = mocker.patch('src.controllers.LoanController.LoanModel')
    mock_loan_model_instance = mock_loan_model.return_value
    mock_loan_model_instance.decrease_stock.return_value = "Stock decreased"
    mock_loan_model_instance.create_loan.return_value = "Loan created"

    loan_controller = LoanController()
    book_id = "Book Test"
    user_id = "User Test"
    loan_date = "2024-01-01"

    response = loan_controller.create_loan(book_id, user_id, loan_date)

    assert response == {
        'status_code': 200,
        'response': 'Loan created successfully',
        'result': "Loan created"
    }

    mock_loan_model_instance.decrease_stock.assert_called_once_with(book_id, 1)
    mock_loan_model_instance.create_loan.assert_called_once_with(book_id, user_id, loan_date)


def test_create_loan_no_stock(mocker):
    mock_loan_model = mocker.patch('src.controllers.LoanController.LoanModel')
    mock_loan_model_instance = mock_loan_model.return_value
    mock_loan_model_instance.decrease_stock.return_value = "Error: No stock available"

    loan_controller = LoanController()
    book_id = "Book Test"
    user_id = "User Test"
    loan_date = "2024-01-01"

    response = loan_controller.create_loan(book_id, user_id, loan_date)

    assert response == {
        'status_code': 409,
        'response': 'No stock available'
    }

    mock_loan_model_instance.decrease_stock.assert_called_once_with(book_id, 1)
    mock_loan_model_instance.create_loan.assert_not_called()


def test_create_loan_exception(mocker):
    mock_loan_model = mocker.patch('src.controllers.LoanController.LoanModel')
    mock_loan_model_instance = mock_loan_model.return_value
    mock_loan_model_instance.create_loan.side_effect = Exception("Mocked exception")

    loan_controller = LoanController()
    book_id = "Book Test"
    user_id = "User Test"
    loan_date = "2024-01-01"

    response = loan_controller.create_loan(book_id, user_id, loan_date)

    assert response == {
        'status_code': 500,
        'response': 'Error creating loan: Mocked exception'
    }

    mock_loan_model_instance.decrease_stock.assert_called_once_with(book_id, 1)
    mock_loan_model_instance.create_loan.assert_called_once_with(book_id, user_id, loan_date)


def test_final_loan_success(mocker):
    mock_loan_model = mocker.patch('src.controllers.LoanController.LoanModel')
    mock_loan_model_instance = mock_loan_model.return_value
    mock_loan_model_instance.final_loan.return_value = True

    loan_controller = LoanController()
    loan_id = "Loan Test"

    response = loan_controller.final_loan(loan_id)

    assert response == {
        'status_code': 200,
        'response': 'Loan finalized successfully'
    }

    mock_loan_model_instance.final_loan.assert_called_once_with(loan_id)


def test_final_loan_failed(mocker):
    mock_loan_model = mocker.patch('src.controllers.LoanController.LoanModel')
    mock_loan_model_instance = mock_loan_model.return_value
    mock_loan_model_instance.final_loan.return_value = "Error: Loan finalization failed"

    loan_controller = LoanController()
    loan_id = "Loan Test"

    response = loan_controller.final_loan(loan_id)

    assert response == {
        'status_code': 400,
        'response': 'Loan finalization failed: Error: Loan finalization failed'
    }

    mock_loan_model_instance.final_loan.assert_called_once_with(loan_id)


def test_final_loan_exception(mocker):
    mock_loan_model = mocker.patch('src.controllers.LoanController.LoanModel')
    mock_loan_model_instance = mock_loan_model.return_value
    mock_loan_model_instance.final_loan.side_effect = Exception("Mocked exception")

    loan_controller = LoanController()
    loan_id = "Loan Test"

    response = loan_controller.final_loan(loan_id)

    assert response == {
        'status_code': 500,
        'response': 'Error finalizing loan: Mocked exception'
    }

    mock_loan_model_instance.final_loan.assert_called_once_with(loan_id)


def test_get_overdue_loans_success(mocker):
    mock_loan_model = mocker.patch('src.controllers.LoanController.LoanModel')
    mock_loan_model_instance = mock_loan_model.return_value
    mock_loan_model_instance.get_overdue_loans.return_value = [{'loan_id': 'Loan Test', 'user_id': 'User Test'}]

    loan_controller = LoanController()

    response = loan_controller.get_overdue_loans()

    assert response == {
        'status_code': 200,
        'response': 'Overdue loans found',
        'result': [{'loan_id': 'Loan Test', 'user_id': 'User Test'}]
    }

    mock_loan_model_instance.get_overdue_loans.assert_called_once_with()


def test_get_overdue_loans_not_found(mocker):
    mock_loan_model = mocker.patch('src.controllers.LoanController.LoanModel')
    mock_loan_model_instance = mock_loan_model.return_value
    mock_loan_model_instance.get_overdue_loans.return_value = []

    loan_controller = LoanController()

    response = loan_controller.get_overdue_loans()

    assert response == {
        'status_code': 404,
        'response': 'No overdue loans found'
    }

    mock_loan_model_instance.get_overdue_loans.assert_called_once_with()


def test_get_overdue_loans_exception(mocker):
    mock_loan_model = mocker.patch('src.controllers.LoanController.LoanModel')
    mock_loan_model_instance = mock_loan_model.return_value
    mock_loan_model_instance.get_overdue_loans.side_effect = Exception("Mocked exception")

    loan_controller = LoanController()

    response = loan_controller.get_overdue_loans()

    assert response == {
        'status_code': 500,
        'response': 'Error fetching overdue loans: Mocked exception'
    }

    mock_loan_model_instance.get_overdue_loans.assert_called_once_with()


def test_notify_overdue_loans_success(mocker):
    mock_loan_model = mocker.patch('src.controllers.LoanController.LoanModel')
    mock_loan_model_instance = mock_loan_model.return_value
    mock_loan_model_instance.notify_overdue_loans.return_value = None

    loan_controller = LoanController()

    response = loan_controller.notify_overdue_loans()

    assert response == {
        'status_code': 200,
        'response': 'Overdue loans notified'
    }

    mock_loan_model_instance.notify_overdue_loans.assert_called_once_with()


def test_notify_overdue_loans_exception(mocker):
    mock_loan_model = mocker.patch('src.controllers.LoanController.LoanModel')
    mock_loan_model_instance = mock_loan_model.return_value
    mock_loan_model_instance.notify_overdue_loans.side_effect = Exception("Mocked exception")

    loan_controller = LoanController()

    response = loan_controller.notify_overdue_loans()

    assert response == {
        'status_code': 500,
        'response': 'Error notifying overdue loans: Mocked exception'
    }

    mock_loan_model_instance.notify_overdue_loans.assert_called_once_with()
