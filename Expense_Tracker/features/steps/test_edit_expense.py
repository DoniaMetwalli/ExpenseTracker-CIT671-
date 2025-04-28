import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'expense_tracker.settings')
django.setup()

from expenses.models import Expense
from behave import given, when, then


@given('I have an existing expense titled "{title}" with amount "{amount}"')
def step_impl(context, title, amount):
    Expense.objects.create(title=title, amount=amount)

@when('I edit the expense to change the title to "{new_title}" and amount to "{new_amount}"')
def step_impl(context, new_title, new_amount):
    expense = Expense.objects.first()
    expense.title = new_title
    expense.amount = new_amount
    expense.save()

# @then('I should see "{title}" with amount "{amount}" in the expense list')
# def step_impl(context, title, amount):
#     expense = Expense.objects.get(title=title)
#     assert str(expense.amount) == amount
