from behave import given, when, then

@given('I am on the add expense page')
def step_impl(context):
    pass

@when('I enter "{title}" as the title and "{amount}" as the amount')
def step_impl(context, title, amount):
    pass

@when('I submit the form')
def step_impl(context):
    pass

@then('I should see "{title}" in the expense list')
def step_impl(context, title):
    pass
