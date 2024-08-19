Feature: Get book by author
  Scenario: Search for a book in the database by its author
    Given The librarian wants to search for a book in the database by its author
    When The librarian provides the author to the system to obtain the book data
    Then The librarian receives the message 'Book found' in database

   Scenario: Search for a book in the database using an incorrect author
     Given Librarian wants to search for a book in the database by incorrect author
     When The librarian provides the incorrect author to the system to obtain the book data
     Then The librarian receives the message 'Book not found' in database

   Scenario: Search for a book in the database by its author, no connection to database
    Given The librarian wants to search for a book in the database by correct author
    When The librarian provides the author to the system to obtain the book
    Then The librarian should receive an error message 'Error finding author of the Book:'
