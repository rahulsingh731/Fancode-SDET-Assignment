Feature: Validate todo completion for FanCode users

  Scenario: All users from FanCode city should have completed more than 50% of their tasks
    Given I have the list of users
    And I filter users from FanCode city
    When I fetch their todos
    Then I should see that all users from FanCode have more than 50% of tasks completed
