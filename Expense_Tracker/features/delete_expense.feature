Feature: Delete Expense

  Scenario: User deletes an existing expense
    Given I have an existing expense titled "Coffee" with amount "5"
    When I delete the expense
    Then I should not see "Coffee" in the expense list
