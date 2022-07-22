Feature: Login Feature

  Scenario Outline: Verify that user is able to log in as "<username>"
    When user is on login page
    And user types in "<username>" as username
    And user types in "<password>" as password
    And user clicks login button
    Then user is logged in
    Examples:
    | username                  | password     |
    | standard_user             | secret_sauce |
    | problem_user              | secret_sauce |
    | performance_glitch_user   | secret_sauce |


  Scenario: Verify that user is not able to log in with invalid username
    When user is on login page
    And user types in "invalid_user" as username
    And user types in "secret_sauce" as password
    And user clicks login button
    Then error message "Epic sadface: Username and password do not match any user in this service" shows up


  Scenario: Verify that user is not able to log in with invalid password
    When user is on login page
    And user types in "standard_user" as username
    And user types in "invalid_sauce" as password
    And user clicks login button
    Then error message "Epic sadface: Username and password do not match any user in this service" shows up


  Scenario: Verify that a locked out user is not able to log in
    When user is on login page
    And user types in "locked_out_user" as username
    And user types in "secret_sauce" as password
    And user clicks login button
    Then error message "Epic sadface: Sorry, this user has been locked out." shows up
