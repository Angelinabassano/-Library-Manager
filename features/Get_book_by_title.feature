Feature: Get book by title
  Scenario: Search for a book in the database by its title
    Given The librarian wants to search for a book in the database by its title
    When The librarian provides the title to the system to obtain the book data
    Then The librarian receives the message 'Book found' in DB

   Scenario: Search for a book in the database using an incorrect title
     Given The librarian wants to search for a book in the database by its incorrect title
     When The librarian provides the incorrect title to the system to obtain the book data
     Then The librarian receives the message 'Book not found' in DB

   Scenario: Search for a book in the database by its title, no connection to DB
    Given The librarian wants to search for a book in the database by correct title
    When The librarian provides the tiitle to the system to obtain the book
    Then The librarian should receive an error message 'Error finding the title of the Book :'
