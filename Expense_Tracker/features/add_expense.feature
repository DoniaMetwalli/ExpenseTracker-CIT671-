Feature: Add Expense

  Scenario: User adds a valid expense
    Given I am on the add expense page
    When I enter "Snacks" as the title and "15" as the amount
    And I submit the form
    Then I should see "Snacks" in the expense list
