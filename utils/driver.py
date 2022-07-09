from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from webdriver_manager.firefox import GeckoDriverManager


class Driver:

    def __init__(self):
        self.driver = None

    def get_driver(self) -> webdriver:
        if self.driver is None:
            firefox_options = FirefoxOptions()
            firefox_options.add_argument("--detach")

            self.driver = webdriver.Firefox(
                executable_path=GeckoDriverManager().install(),
                options=firefox_options)
            self.driver.maximize_window()

        return self.driver

    def close_driver(self):
        if self.driver is not None:
            self.driver.close()
