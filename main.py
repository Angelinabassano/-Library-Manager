from src.controllers.BookController import BookController
from src.controllers.UserController import UserController
from src.controllers.CategoryController import CategoryController
from src.controllers.LoanController import LoanController
from datetime import date


def main():

    user_controller = UserController()
    book_controller = BookController()
    category_controller = CategoryController()
    loan_controller = LoanController()

    print("\nCreating a new user ...\n")
    user_id = 16
    first_name = "Leo"
    last_name = "Fieie"
    email = "susana@gmail.com"
    phone_number = 654779544
    address = "Avenida loca 4"
    register = user_controller.create_user(user_id, first_name, last_name, email, phone_number, address)
    print(register)

    print("\nSearching user....\n")
    user_id = 1
    user = user_controller.get_user(user_id)
    print(user)

    print("\nUpdating  the user with ID ...\n")
    user_id = 16
    first_name = "Julia"
    last_name = "Beltran"
    phone_number = 883456750
    address = "Calle Principal 333"
    update = user_controller.update_user(user_id, first_name, last_name, phone_number, address)
    print(update)

    print('\nDeleting user with ID ...')
    user_id = 17
    delete = user_controller.delete_user(user_id,)
    print(delete)

    print("\nVerifying data ...")
    book_id = 1
    title = "El Quijote"
    author = "Miguel de Cervantes"
    category_id = 6
    data_book = book_controller.verify_data(book_id, title, author, category_id, )
    print(data_book)

    print("\nCreating a new book ...\n")
    book_id = 39
    title = "El Poder de las Palabras: Cómo cambiar tu cerebro conversando."
    author = "Mariano Sigman"
    category_id = 5
    stock = 5
    book = book_controller.create_book(book_id, title, author, category_id, stock)
    print(book)

    print("\nSearching the book with ID ...\n")
    book_id = 16
    find = book_controller.get_book_by_id(book_id)
    print(find)

    print("\nSearching by author....\n")
    author = "J.K. Rowling"
    find_author = book_controller.get_book_by_author(author)
    print(find_author)

    print("\nSearching the book with title..\n")
    title = "La Odisea"
    find_title = book_controller.get_book_by_title(title)
    print(find_title)

    print("\nUpdating the book with ID ...\n")
    book_id = 50
    title = "El Quijote"
    author = "Miguel de Cervantes Saavedra"
    category_id = 6
    stock = 1
    modify = book_controller.update_book(book_id, title, author, category_id, stock)
    print(modify)

    print("\nIncreasing the book stock with ID ...\n")
    book_id = 39
    stock = 2
    increment = book_controller.update_book_by_stock_increment(stock, book_id, )
    print(increment)

    print("\nDecreasing the book stock with ID ...\n")
    book_id = 39
    stock_decrement = 1
    decrease = book_controller.update_book_by_stock_decrease(book_id, stock_decrement, )
    print(decrease)

    print("\nDeletting book with ID ...")
    book_id = 40
    delete = book_controller.delete_book(book_id, True)
    print(delete)

    print('\nVerifying category….\n')
    category_id = 3
    category_name = 'Romance'
    find = category_controller.verify_category(category_id, category_name)
    print(find)

    print('\nCreate new category….')
    category_id = 12
    category_name = 'Cocina'
    newCategory = category_controller.create_category(category_id, category_name)
    print(newCategory)

    print('\nSearching category by id…')
    category_id = 4
    result = category_controller.get_category_by_id(category_id)
    print(result)

    print('\nSearching category by name….')
    category_name = 'Neurociencia'
    name_category = category_controller.get_category_by_name(category_name)
    print(name_category)

    print('\nUpdating category….')
    category_id = 12
    category_name = 'Cocina Italiana'
    updateCat = category_controller.update_category(category_id, category_name)
    print(updateCat)

    print('\nDelete category…')
    category_id = 13
    result_del = category_controller.delete_category(category_id, True)
    print(result_del)

    print('\nCreating a new loan…')
    loan_id = 1
    book_id = 2
    user_id = 2
    loan_date = date.today()
    create_loan = loan_controller.create_loan(loan_id, book_id, user_id, loan_date)
    print(create_loan)

    print('\nCreating final_loan')
    loan_id = 1
    final_date = date.today()
    create_final_loan = loan_controller.final_loan(loan_id, final_date)
    print(create_final_loan)

    print('\nSearching the books with an overdue date....\n')
    result_overdue = loan_controller.get_overdue_loans()
    print(result_overdue)

    print('\nNotify overdue_loans')
    notify_overdue = loan_controller.notify_overdue_loans()
    print(notify_overdue)

    print("\nDeleting a loan..")
    loan_id = 4
    delete_loan = loan_controller.delete_loan(loan_id)
    print(delete_loan)


if __name__ == "__main__":
 main()
