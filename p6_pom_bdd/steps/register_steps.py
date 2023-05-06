from behave import *


@given('I am on the Register Page')
def step_impl(context):
    context.register_page.navigate_to_register_page()


@when('I click on the Register button')
def step_impl(context):
    context.register_page.click_register_button()


@then('First name error is displayed')
def step_impl(context):
    assert context.register_page.is_first_name_error_displayed()


@then('Last name error is displayed')
def step_impl(context):
    assert context.register_page.is_last_name_error_displayed()


@then('Email error is displayed')
def step_impl(context):
    assert context.register_page.is_email_error_displayed()


@then('Password error is displayed')
def step_impl(context):
    assert context.register_page.is_password_error_displayed()


@then('Confirm password error is displayed')
def step_impl(context):
    assert context.register_page.is_password_confirm_error_displayed()