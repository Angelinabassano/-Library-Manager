import pytest
from unittest.mock import MagicMock
from src.controllers.BookController import BookController


def test_verify_data_success(mocker):
    mock_book_model = mocker.patch('src.controllers.BookController.BookModel')
    mock_book_model_instance = mock_book_model.return_value
    mock_book_model_instance.verify_data.return_value = {'book_id': 'Book_id Test', 'title': 'Title Test',
                                                         'author': 'Author Test', 'category_id': 'Category Test'}
    book_controller = BookController()
    book_id = "Book_id Test"
    title = "Title Test"
    author = "Author Test"
    category_id = "Category Test"

    response = book_controller.verify_data(book_id, title, author, category_id)
    assert response == {
        'status_code': 200,
        'response': 'Verify data',
        'result': {'book_id': 'Book Test', 'title': 'Title Test', 'author': 'Author Test',
                   'category_id': 'Category Test'}
    }

    mock_book_model_instance.verify_data.assert_called_once_with(book_id, title, author, category_id)


def test_verify_data_not_found(mocker):
    mock_book_model = mocker.patch('src.controllers.BookController.BookModel')
    mock_book_model_instance = mock_book_model.return_value
    mock_book_model_instance.verify_data.return_value = None
    book_controller = BookController()
    book_id = "Book_id Test"
    title = "Title Test"
    author = "Author Test"
    category_id = "Category Test"

    response = book_controller.verify_data(book_id, title, author, category_id)

    assert response == {
        'status_code': 404,
        'response': 'Don’t verify data'
    }


def test_verify_data_exception(mocker):
    mock_book_model = mocker.patch('src.controllers.BookController.BookModel')
    mock_book_model_instance = mock_book_model.return_value
    mock_book_model_instance.verify_data.side_effect = Exception("Mocked exception")

    book_controller = BookController()
    book_controller.book_model = mock_book_model_instance
    book_id = "Book_id Test"
    title = "Title Test"
    author = "Author Test"
    category_id = "Category Test"

    response = book_controller.verify_data(book_id, title, author, category_id)

    assert response == {
        'status_code': 500,
        'response': 'Error verifying data: Mocked exception'
    }


def test_create_book_success(mocker):
    mock_book_model = mocker.patch('src.controllers.BookController.BookModel')
    mock_book_model_instance = mock_book_model.return_value
    mock_book_model_instance.create_book.return_value = None
    book_controller = BookController()
    book_id = "Book_id Test"
    title = "Title Test"
    author = "Author Test"
    category_id = "Category Test"
    stock = 10

    response = book_controller.create_book(book_id, title, author, category_id, stock)

    expected_result = {
        'result': f'{"Book_id Test", "Title Test", "Author Test", "Category Test", 10}'
    }
    assert response == expected_result
    mock_book_model_instance.create_book.assert_called_once_with(book_id, title, author, category_id, stock)


def test_create_book_failure(mocker):
    mock_book_model = mocker.patch('src.controllers.BookController.BookModel')
    mock_book_model_instance = mock_book_model.return_value
    mock_book_model_instance.create_book.side_effect = Exception("Mocked exception")
    book_controller = BookController()
    book_id = "Book_id Test"
    title = "Title Test"
    author = "Author Test"
    category_id = "Category Test"
    stock = 10

    response = book_controller.create_book(book_id, title, author, category_id, stock)

    assert response == {
        'status_code': 500,
        'response': 'Error when creating the book: Mocked exception'
    }
    mock_book_model_instance.create_book.assert_called_once_with(book_id, title, author, category_id, stock)
