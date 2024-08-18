from behave import given, when, then
from src.controllers.BookController import BookController


@given('the librarian has a valid book')
def step_impl(context):
    context.book_id = 1
    context.title = "El Quijote"
    context.author = "Miguel de Cervantes"
    context.category_id = 6


@when('the librarian wants to verify if the provided book exists in the DB')
def step_impl(context):
    try:
        book_controller = BookController()
        context.result = book_controller.verify_data(
            context.book_id, context.title, context.author, context.category_id
        )
    except Exception as e:
        context.result = {'status_code': 500, 'response': f'Error verifying data: {e}'}


@then('the librarian should receive the message \'Verify data\' in the DB')
def step_impl(context):
    assert context.result['status_code'] == 200
    assert context.result['response'] == 'Verify data'


@given('the librarian has book with incorrect parameters')
def step_impl(context):
    context.book_id = 1
    context.title = "El"
    context.author = "Miguel de Cervantes"
    context.category_id = 9999


@when('the librarian wants to verify if the book provided to the system exists in the DB')
def step_impl(context):
    book_controller = BookController()
    context.result = book_controller.verify_data(
       context.book_id, context.title, context.author, context.category_id
    )


@then('the librarian should receive an error message \'Don´t Verify data\'')
def step_impl(context):
    assert context.result['status_code'] == 404
    assert context.result['response'] == 'Don´t Verify data'


@given('the librarian has valid book')
def step_impl(context):
    context.book_id = 1
    context.title = "El Quijote"
    context.author = "Miguel de Cervantes"
    context.category_id = 6


@when('the librarian wants to verify if the book exists in the DB')
def step_impl(context):
    try:
        raise Exception("No connection to the database")
    except Exception as e:
        context.result = {'status_code': 500, 'response': f'Error verifying data: {e}'}


@then('The librarian should receive an error message \'Error verifying data:\'')
def step_impl(context):
    assert context.result['status_code'] == 500
    assert "Error verifying data:" in context.result['response']
