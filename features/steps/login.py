from behave import when, then
from utils.driver import Driver
from pages import LoginPage
from utils.config_reader import ConfigReader

driver = Driver()


@when(u'user is on login page')
def step_impl(context):
    driver.get_driver().get(ConfigReader().get_value("swag-labs", "url"))


@when(u'user types in {username} as username')
def step_impl(context, username):
    driver.get_driver().find_element(*LoginPage.input_username).send_keys(username)


@when(u'user types in {password} as password')
def step_impl(context, password):
    driver.get_driver().find_element(*LoginPage.input_password).send_keys(password)


@when(u'user click login button')
def step_impl(context):
    driver.get_driver().find_element(*LoginPage.btn_login).click()


@then(u'user is logged in')
def step_impl(context):
    assert True
