from selenium.webdriver.common.by import By


class LoginPage:
    input_username = (By.ID, "user-name")
    input_password = (By.ID, "password")
    btn_login = (By.ID, "login-button")
    div_error_message = (By.XPATH, "//div[contains(@class, 'error-message-container')]/*[text()="
                                   "'Epic sadface: Username and password do not match any user in this service']")

    @staticmethod
    def get_err_msg_web_element(err_msg):
        print(err_msg)
        return By.XPATH, "//div[contains(@class, 'error-message-container')]/*[text()='" + err_msg + "']"
