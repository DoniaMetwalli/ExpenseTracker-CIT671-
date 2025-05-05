import pytest
import datetime
from expenses.models import Expense


@pytest.mark.django_db
def test_expense_creation():
    expense = Expense.objects.create(
        title="Groceries",
        amount=50.00,
        category = "Monthly Groceries",
        date=datetime.date(2024, 1, 1) 
    )
    assert expense.title == "Groceries"
    assert expense.amount == 50.00
    assert expense.category == "Monthly Groceries"
    assert expense.date == datetime.date(2024, 1, 1)
