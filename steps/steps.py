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

