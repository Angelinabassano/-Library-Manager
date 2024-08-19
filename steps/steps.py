from behave import given, when, then
from src.controllers.BookController import BookController
from src.controllers.LoanController import LoanController


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

    @given('the library wants to make a loan.')
    def step_impl(context):
        context.book_id = 1
        context.user_id = 2

    @when('the librarian wants to check if the provided loan can be made in the DB')
    def step_impl(context):
        try:
            loan_controller = LoanController()
            context.result = loan_controller.verify_data(
                context.book_id, context.user_id
            )
        except Exception as e:
            context.result = {'status_code': 500, 'response': f'Error verifying data: {e}'}

    @then('the librarian should receive the \'Verify data\' message in the DB')
    def step_impl(context):
        assert context.result['status_code'] == 200
        assert context.result['response'] == 'Verify data'
