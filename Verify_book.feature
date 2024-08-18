Feature:Verify book
  Scenario: Valid book to check if there is a book registered in the DB
    Given the librarian has a valid book
    When the librarian wants to verify if the provided book exists in the DB
    Then the librarian should receive the message 'Verify data' in the DB

  Scenario: Invalid book to check if there is a record of it in the DB
    Given the librarian has book with incorrect parameters
    When the librarian wants to verify if the book provided to the system exists in the DB
    Then the librarian should receive an error message 'Don´t Verify data'

  Scenario: Valid book to verify, no connection to DB
    Given the librarian has valid book
    When the librarian wants to verify if the book exists in the DB
    Then the librarian should receive an error message 'Error verifying data:'
