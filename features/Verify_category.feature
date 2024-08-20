Feature:Verify Category
  Scenario: Verify that the category exists
    Given the librarian wants to verify that a category exists
    When the librarian wants to check if the provided loan can be made in the database
    Then the librarian should receive the message 'Verify category' in the database

  Scenario: The category cannot be verified in the database
    Given the librarian checks a category with incorrect parameters
    When the librarian wants to verify if the category provided to the system exists in the database
    Then the librarian should receive an error message 'Don’t Verify category'

  Scenario: Valid category to verify, without connection to database
    Given the librarian has a valid category
    When the librarian wants to check if the category exists in the database
    Then the librarian should receive an error message 'Error verifying category:'