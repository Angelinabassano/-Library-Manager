import pytest
from unittest.mock import MagicMock
from src.controllers.UserController import UserController


def test_create_user_success(mocker):
    mock_user_model = mocker.patch('src.controllers.UserController.UsersModels')
    mock_user_model_instance = mock_user_model.return_value
    mock_user_model_instance.verify_user.return_value = False
    mock_user_model_instance.create_user.return_value = None

    user_controller = UserController()
    user_id = "user_id Test"
    first_name = "First_name Test"
    last_name = "Last_name Test"
    email = "Email Test"
    phone_number = "Phone_number Test"
    address = "Address Test"

    response = user_controller.create_user(user_id, first_name, last_name, email, phone_number, address)

    expect_result = {
        'status_code': 200,
        'response': 'User create successfully',
        'result': [user_id, first_name, last_name, email, phone_number, address]
    }

    assert response == expect_result
    mock_user_model_instance.create_user.assert_called_once_with(user_id, first_name, last_name, email, phone_number, address)


def test_create_user_failed(mocker):
    mock_user_model = mocker.patch('src.controllers.UserController.UsersModels')
    mock_user_model_instance = mock_user_model.return_value
    mock_user_model_instance.verify_user.return_value = True

    user_controller = UserController()
    user_id = "user_id Test"
    first_name = "First_name Test"
    last_name = "Last_name Test"
    email = "Email Test"
    phone_number = "Phone_number Test"
    address = "Address Test"

    response = user_controller.create_user(user_id, first_name, last_name, email, phone_number, address)

    expect_result = {
        'status_code': 400,
        'response': 'User already exists',
        'result': [user_id, first_name, last_name, email, phone_number, address]
    }

    assert response == expect_result
    mock_user_model_instance.verify_user.assert_called_once_with(email)
    mock_user_model_instance.create_user.assert_not_called()


def test_update_user_success(mocker):
    mock_user_model = mocker.patch('src.controllers.UserController.UsersModels')
    mock_user_model_instance = mock_user_model.return_value
    mock_user_model_instance.get_user.return_value = True
    mock_user_model_instance.update_user.return_value = None

    user_controller = UserController()
    user_id = "1 Test"
    first_name = "Juan Test"
    last_name = "Perez Test"
    phone_number = "123456789 Test"
    address = "Calle principal 123 Test"

    response = user_controller.update_user(user_id, first_name, last_name, phone_number, address)

    expect_result = {
        'status_code': 200,
        'response': 'User updated successfully'
    }

    assert response == expect_result
    mock_user_model_instance.get_user.assert_called_once_with(user_id)
    mock_user_model_instance.update_user.assert_called_once_with(user_id, first_name, last_name, phone_number, address)


def test_update_user_not_found(mocker):
    mock_user_model = mocker.patch('src.controllers.UserController.UsersModels')
    mock_user_model_instance = mock_user_model.return_value
    mock_user_model_instance.get_user.return_value = False

    user_controller = UserController()
    user_id = "1 Test"
    first_name = "Juan Test"
    last_name = "Perez Test"
    phone_number = "123456789 Test"
    address = "Calle principal 123 Test"

    response = user_controller.update_user(user_id, first_name, last_name, phone_number, address)

    expect_result = {
        'status_code': 404,
        'response': 'User not found'
    }

    assert response == expect_result
    mock_user_model_instance.get_user.assert_called_once_with(user_id)
    mock_user_model_instance.update_user.assert_not_called()


def test_delete_user_success(mocker):
    mock_user_model = mocker.patch('src.controllers.UserController.UsersModels')
    mock_user_model_instance = mock_user_model.return_value
    mock_user_model_instance.get_user.return_value = True
    mock_user_model_instance.delete_user.return_value = None

    user_controller = UserController()
    user_id = "1 Test"

    response = user_controller.delete_user(user_id)

    expect_result = {
        'status_code': 200,
        'response': 'User successfully deleted'
    }

    assert response == expect_result
    mock_user_model_instance.get_user.assert_called_once_with(user_id)
    mock_user_model_instance.delete_user.assert_called_once_with(user_id)


def test_delete_user_not_found(mocker):
    mock_user_model = mocker.patch('src.controllers.UserController.UsersModels')
    mock_user_model_instance = mock_user_model.return_value
    mock_user_model_instance.get_user.return_value = False

    user_controller = UserController()
    user_id = "1 Test"

    response = user_controller.delete_user(user_id)

    expect_result = {
        'status_code': 404,
        'response': 'User not found'
    }

    assert response == expect_result
    mock_user_model_instance.get_user.assert_called_once_with(user_id)
    mock_user_model_instance.delete_user.assert_not_called()
