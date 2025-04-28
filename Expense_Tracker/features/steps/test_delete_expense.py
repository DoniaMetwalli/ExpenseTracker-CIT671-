import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'expense_tracker.settings')
django.setup()

from expenses.models import Expense
from behave import given, when, then


@when('I delete the expense')
def step_impl(context):
    expense = Expense.objects.first()
    expense.delete()

@then('I should not see "{title}" in the expense list')
def step_impl(context, title):
    expenses = Expense.objects.filter(title=title)
    assert not expenses.exists()
