Feature: Check Loan
  Scenario: Verify that a loan can be made
    Given the library wants to make a loan.
    When the librarian wants to check if the provided loan can be made in the database
    Then the librarian should receive the 'Verify data' message in the database

  Scenario: Cannot make the loan in the DB
    Given the librarian has loan with incorrect parameters
    When the librarian wants to verify if data provided to the system exists in the database
    Then the librarian should receive an error message 'Don´t Verify data'

  Scenario: Valid loan to make, without connection to DB
    Given the librarian has valid data to make the loan
    When the librarian wants to check if the data exists in the database
    Then the librarian should receive an error message 'Error verifying data:'