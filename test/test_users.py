import pytest
from unittest.mock import MagicMock
from src.controllers.UserController import UserController


def test_create_user_success(mocker):
    mock_user_model = mocker.patch('src.controllers.UserController.UsersModels')
    mock_user_model_instance = mock_user_model.return_value
    mock_user_model_instance.verify_user.return_value = False
    mock_user_model_instance.create_user.return_value = None

    user_controller = UserController()
    first_name = "First_name Test"
    last_name = "Last_name Test"
    email = "Email Test"
    phone_number = "Phone_number Test"
    address = "Address Test"

    response = user_controller.create_user(first_name, last_name, email, phone_number, address)

    expect_result = {
        'status_code': 200,
        'response': 'El usuario se creo de manera exitosa',
        'result': [first_name, last_name, email, phone_number, address]
    }

    assert response == expect_result
    mock_user_model_instance.create_user.assert_called_once_with(first_name, last_name, email, phone_number, address)


def test_create_user_failure(mocker):
    mock_user_model = mocker.patch('src.controllers.UserController.UsersModels')
    mock_user_model_instance = mock_user_model.return_value
    mock_user_model_instance.verify_user.return_value = True

    user_controller = UserController()
    first_name = "First_name Test"
    last_name = "Last_name Test"
    email = "Email Test"
    phone_number = "Phone_number Test"
    address = "Address Test"

    response = user_controller.create_user(first_name, last_name, email, phone_number, address)

    expect_result = {
        'status_code': 400,
        'response': 'El usuario ya existe',
        'result': [first_name, last_name, email, phone_number, address]
    }

    assert response == expect_result
    mock_user_model_instance.verify_user.assert_called_once_with(email)
    mock_user_model_instance.create_user.assert_not_called()
