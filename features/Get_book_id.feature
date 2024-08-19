Feature: Get Book by id
  Scenario: Search for a book in the database by its id
    Given The librarian wants to search for a book in the database by its id
    When The librarian provides the id to the system to obtain the book data
    Then The librarian receives the message 'Book_id found' in DB

  Scenario: Search for a book in the database using an incorrect book_id
    Given The librarian wants to search for a book in the database by incorrect book_id
    When The librarian provides the incorrect book_id to the system to obtain the book data
    Then The librarian receives the message 'Book_id not found' in DB

  Scenario:  Search for a book in the database by its id, no connection to DB
    Given The librarian wants to search for a book in the database by correct book_id
    When The librarian provides the book_id to the system to obtain the book
    Then The librarian should receive an error message 'Error finding book_id:'