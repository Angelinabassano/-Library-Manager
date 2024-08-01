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
