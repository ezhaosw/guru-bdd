from behave import given, when, then
from steps.bank_home import BankHome


@given('I am on the home page')
def user_on_page(context):
    context.home = BankHome(context.driver)


@when('I type "{user_id}" in the userid field')
def user_enters_id(context, user_id):
    context.home.enter_id(user_id)


@when('I type "{pwd}" in the password field')
def user_enters_pwd(context, pwd):
    context.home.enter_password(pwd)


@when('I press the "login" button')
def user_presses_login(context):
    context.profile = context.home.login()


@then('I will see the "customer" page')
def user_logged_in(context):
    assert context.profile.on_page()


@given('I am on the "customer" page')
def user_on_profile(context):
    user_logged_in(context)


@when('I click the "Balance Enquiry" link')
def user_clicks_balance_enquiry(context):
    context.enquiry = context.profile.check_balance()


@when('I see the "Balance Enquiry Form" page')
def user_on_enquiry_page(context):
    assert context.enquiry.on_page()


@when('I select "{account_id}" from the drop-down menu')
def user_selects_account(context, account_id):
    context.enquiry.select_account(account_id)


@when('I press the "submit" button')
def user_submits_account_choice(context):
    context.balance = context.enquiry.submit_choice()


@then('I will see the "Balance Details" page')
def user_on_balance_page(context):
    assert context.balance.on_page()
