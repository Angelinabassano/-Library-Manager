Feature: Verify user by ID
  As a user of the system
  I want to search for a user by their ID
  So that I can verify if the user exists in the system

  Scenario: Successfully find an existing user by ID
    Given a user exists with ID "1"
    When I search for the user by ID "1"
    Then the user should be found with status code 200
    And the response should include "user_id found"

  Scenario: Fail to find a non-existent user by ID
    Given no user exists with ID "2"
    When I search for the user by ID "2"
    Then the user should not be found with status code 404
    And the response should include "user_id not found"