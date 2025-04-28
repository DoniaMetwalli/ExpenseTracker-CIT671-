Feature: Edit Expense

  Scenario: User edits an existing expense
    Given I have an existing expense titled "Lunch" with amount "20"
    When I edit the expense to change the title to "Dinner" and amount to "25"
    Then I should see "Dinner" with amount "25" in the expense list
