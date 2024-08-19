import pytest
from unittest.mock import MagicMock
from src.controllers.CategoryController import CategoryController


def test_verify_category_success(mocker):
    mock_category_model = mocker.patch('src.controllers.CategoryController.CategoryModel')
    mock_category_model_instance = mock_category_model.return_value
    mock_category_model_instance.verify_category.return_value = {'category_id': 'Category_id',
                                                                 'category_name': 'Category Test'}

    category_controller = CategoryController()
    category_id = "Category_id"
    category_name = "Category Test"

    response = category_controller.verify_category(category_id, category_name)

    assert response == {
        'status_code': 200,
        'response': 'Verify category',
        'result': {'category_id': 'Category_id', 'category_name': 'Category Test'}
    }
    mock_category_model_instance.verify_category.assert_called_once_with(category_id, category_name)


def test_verify_data_not_found(mocker):
    mock_category_model = mocker.patch('src.controllers.CategoryController.CategoryModel')
    mock_category_model_instance = mock_category_model.return_value
    mock_category_model_instance.verify_category.return_value = None

    category_controller = CategoryController()
    category_id = "Category_id"
    category_name = "Category Test"

    response = category_controller.verify_category(category_id, category_name)

    assert response == {
        'status_code': 404,
        'response': 'Don’t Verify category'
    }


def test_verify_data_exception(mocker):
    mock_category_model = mocker.patch('src.controllers.CategoryController.CategoryModel')
    mock_category_model_instance = mock_category_model.return_value
    mock_category_model_instance.verify_category.side_effect = Exception("Mocked exception")

    category_controller = CategoryController()
    category_id = "Category_id"
    category_name = "Category Test"

    response = category_controller.verify_category(category_id, category_name)

    assert response == {
        'status_code': 500,
        'response': f'Error verifying category: Mocked exception'
    }


def test_create_category_success(mocker):
    mock_category_model = mocker.patch('src.controllers.CategoryController.CategoryModel')
    mock_category_model_instance = mock_category_model.return_value
    mock_category_model_instance.create_category.return_value = None

    category_controller = CategoryController()
    category_id = "Category_id"
    category_name = "Category Test"

    response = category_controller.create_category(category_id, category_name)

    expected_result = {
        'result': f'{'Category_id', 'Category Test'}'
    }
    assert response == expected_result
    mock_category_model_instance.create_category.assert_called_once_with(category_id, category_name)


def test_create_category_failed(mocker):
    mock_category_model = mocker.patch('src.controllers.CategoryController.CategoryModel')
    mock_category_model_instance = mock_category_model.return_value
    mock_category_model_instance.create_category.side_effect = Exception("Mocked exception")

    category_controller = CategoryController()
    category_id = "Category_id"
    category_name = "Category Test"

    response = category_controller.create_category(category_id, category_name)

    assert response == {
        'status_code': 500,
        'response': f'Error when creating the category: Mocked exception'
    }
    mock_category_model_instance.create_category.assert_called_once_with(category_id, category_name)

