Feature: Login Feature

  Scenario Outline: Verify that user is able to log in as "<username>"
    When user types in "<username>" as username
    And user types in "<password>" as password
    And user click login button
    Then user is logged in
    Examples:
    | username                  | password     |
    | standard_user             | secret_sauce |
    | locked_out_user           | secret_sauce |
    | problem_user              | secret_sauce |
    | performance_glitch_user   | secret_sauce |
