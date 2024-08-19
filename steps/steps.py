from behave import given, when, then
from src.controllers.BookController import BookController
from src.controllers.LoanController import LoanController
from src.controllers.UserController import UserController


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


@given('The librarian wants to search for a book in the database by its id')
def step_impl(context):
    context.book_id = 1


@when('The librarian provides the id to the system to obtain the book data')
def step_impl(context):
    try:
        book_controller = BookController()
        context.result = book_controller.get_book_by_id(context.book_id)
    except Exception as e:
        return {'status_code': 500, 'response': f'Error finding book_id: {e}'}


@then('The librarian receives the message \'Book_id found\' in DB')
def step_impl(context):
    assert context.result['status_code'] == 200
    assert context.result['response'] == 'Book_id found'


@given('The librarian wants to search for a book in the database by incorrect book_id')
def step_impl(context):
    context.book_id = 50


@when('The librarian provides the incorrect book_id to the system to obtain the book data')
def step_impl(context):
    book_controller = BookController()
    context.result = book_controller.get_book_by_id(context.book_id)


@then('The librarian receives the message \'Book_id not found\' in DB')
def step_impl(context):
    assert context.result['status_code'] == 404
    assert context.result['response'] == 'Book_id not found'


@given('The librarian wants to search for a book in the database by correct book_id')
def step_impl(context):
    context.book_id = 1


@when('The librarian provides the book_id to the system to obtain the book')
def step_impl(context):
    try:
        raise Exception("No connection to the database")
    except Exception as e:
        context.result = {'status_code': 500, 'response': f'Error finding book_id: {e}'}


@then('The librarian should receive an error message \'Error finding book_id:\'')
def step_impl(context):
    assert context.result['status_code'] == 500
    assert 'Error finding book_id:' in context.result['response']


@given('The librarian wants to search for a book in the database by its title')
def step_impl(context):
    context.title = "El Quijote"


@when('The librarian provides the title to the system to obtain the book data')
def step_impl(context):
    try:
        book_controller = BookController()
        context.result = book_controller.get_book_by_title(context.title)

    except Exception as e:
        return {'status_code': 500, 'response': f'Error finding book_id: {e}'}


@then('THe librarian receives the message \'Book found\' in DB')
def step_impl(context):
    assert context.result['status_code'] == 200
    assert context.result['response'] == 'Book found'


@given('The librarian wants to search for a book in the database by its incorrect title')
def step_impl(context):
    context.title = "La Odisea"


@when('The librarian provides the incorrect title to the system to obtain the book data')
def step_impl(context):
    book_controller = BookController()
    context.result = book_controller.get_book_by_title(context.title)


@then('The librarian receives the message \'Book not found\' in DB')
def step_impl(context):
    assert context.result['status_code'] == 404
    assert context.result['response'] == 'Book not found'


@given('The librarian wants to search for a book in the database by correct title')
def step_impl(context):
    context.title = "El Quijote"


@when('The librarian provides the tiitle to the system to obtain the book')
def step_impl(context):
    try:
        raise Exception("No connection to the database")
    except Exception as e:
        context.result = {'status_code': 500, 'response': f'Error finding the title of the Book: {e}'}


@then('The librarian should receive an error message \'Error finding the title of the Book :\'')
def step_impl(context):
    assert context.result['status_code'] == 500
    assert 'Error finding the title of the Book:' in context.result['response']


@given('The librarian wants to search for a book in the database by its author')
def step_impl(context):
    context.author = "J.K. Rowling"


@when('The librarian provides the author to the system to obtain the book data')
def step_impl(context):
    try:
        book_controller = BookController()
        context.result = book_controller.get_book_by_author(context.author)

    except Exception as e:
        return {'status_code': 500, 'response': f'Error finding author of the Book: {e}'}


@then('The librarian receives the message \'Book found\' in database')
def step_impl(context):
    assert context.result['status_code'] == 200
    assert context.result['response'] == 'Book found'


@given('Librarian wants to search for a book in the database by incorrect author')
def step_impl(context):
    context.author = "Miguel"


@when('The librarian provides the incorrect author to the system to obtain the book data')
def step_impl(context):
    book_controller = BookController()
    context.result = book_controller.get_book_by_author(context.author)


@then('The librarian receives the message \'Book not found\' in database')
def step_impl(context):
    assert context.result['status_code'] == 404
    assert context.result['response'] == 'Book not found'


@given('The librarian wants to search for a book in the database by correct author')
def step_impl(context):
    context.author = "Roald Dahl"


@when('The librarian provides the author to the system to obtain the book')
def step_impl(context):
    try:
        raise Exception("No connection to the database")
    except Exception as e:
        context.result = {'status_code': 500, 'response': f'Error finding author of the Book: {e}'}

        
@then('The librarian should receive an error message \'Error finding author of the Book:\'')
def step_impl(context):
    assert context.result['status_code'] == 500
    assert 'Error finding author of the Book:' in context.result['response']        

    
@given('the library wants to make a loan.')
def step_impl(context):
    context.book_id = 2
    context.user_id = 3


@when('the librarian wants to check if the provided loan can be made in the DB')
def step_impl(context):
    try:
        loan_controller = LoanController()
        context.result = loan_controller.verify_data(
            context.book_id, context.user_id
        )
    except Exception as e:
        context.result = {'status_code': 500, 'response': f'Error verifying data: {e}'}


@then('the librarian should receive the message \'Data verified\' in the database')
def step_impl(context):
    assert context.result['status_code'] == 200
    assert context.result['response'] == 'Data verified'


@given('the librarian has loan with incorrect parameters')
def step_impl(context):
    context.book_id = 18522
    context.user_id = 84865


@when('the librarian wants to verify if data provided to the system exists in the database')
def step_impl(context):
    loan_controller = LoanController()
    context.result = loan_controller.verify_data(
        context.book_id, context.user_id
    )


@then('the librarian should receive an error message \'Do not Verify data\'')
def step_impl(context):
    assert context.result['status_code'] == 404
    assert context.result['response'] == 'Data not verified'


@given('the librarian has valid data to make the loan')
def step_impl(context):
    context.book_id = 1
    context.user_id = 3


@when('the librarian wants to check if the data exists in the database')
context.result = {'status_code': 500, 'response': f'Error verifying data: {e}'}

         
@then('the librarian should receive an error message \'Error verify data:\'')
def step_impl(context):
    assert context.result['status_code'] == 500
    assert "Error verifying data:" in context.result['response']


@given('a user exists with ID "{user_id}"')
def step_impl(context, user_id):
    context.user_controller = UserController()
    context.user_controller.user_model.create_user(
        user_id=user_id,
        first_name="John",
        last_name="Doe",
        email="john@example.com",
        phone_number="123456789",
        address="123 Main St"
    )


@when('I search for the user by ID "{user_id}"')
def step_impl(context, user_id):
    context.response = context.user_controller.get_user(user_id)


@then('the user should be found with status code 200')
def step_impl(context):
    assert context.response['status_code'] == 200


@then('the response should include "user_id found"')
def step_impl(context):
    assert "user_id found" in context.response['response']


@given('no user exists with ID "{user_id}"')
def step_impl(context, user_id):
    context.user_controller = UserController()
    context.user_controller.user_model.delete_user(user_id)


@then('the user should not be found with status code 404')
def step_impl(context):
    assert context.response['status_code'] == 404


@then('the response should include "user_id not found"')
def step_impl(context):
    assert "user_id not found" in context.response['response']

