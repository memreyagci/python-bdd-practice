from behave import when, then
from utils import ConfigReader, Driver
from pages import LoginPage


@when('user is on login page')
def step_impl(context):
    Driver.get_driver().get(ConfigReader().get_value("swag-labs", "url"))


@when('user types in "{username}" as username')
def step_impl(context, username):
    Driver.get_driver().find_element(*LoginPage.input_username).send_keys(username)


@when('user types in "{password}" as password')
def step_impl(context, password):
    Driver.get_driver().find_element(*LoginPage.input_password).send_keys(password)


@when('user clicks login button')
def step_impl(context):
    Driver.get_driver().find_element(*LoginPage.btn_login).click()


@then('user is logged in')
def step_impl(context):
    assert(Driver.get_driver().current_url,"https://www.saucedemo.com/inventory.html")


@then('error message "{err_msg}" shows up')
def step_impl(context, err_msg):
    assert Driver.get_driver().find_element(*LoginPage.get_err_msg_web_element(err_msg)).is_displayed()
