from selenium import webdriver

from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.edge.options import Options as EdgeOptions

from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

from utils.config_reader import ConfigReader


class Driver:

    def __init__(self):
        self.driver = None

    def get_driver(self) -> webdriver:
        browser = ConfigReader().get_value("selenium", "browser")

        if self.driver is None:
            if browser == "firefox":
                firefox_options = FirefoxOptions()
                firefox_options.add_argument("--detach")

                self.driver = webdriver.Firefox(
                    executable_path=GeckoDriverManager().install(),
                    options=firefox_options)

            elif browser == "chrome":
                chrome_options = ChromeOptions()
                chrome_options.add_argument("--detach")

                self.driver = webdriver.Firefox(
                    executable_path=ChromeDriverManager().install(),
                    options=chrome_options)

            elif browser == "edge":
                edge_options = EdgeOptions()
                edge_options.add_argument("--detach")

                self.driver = webdriver.Edge(
                    executable_path=EdgeChromiumDriverManager().install(),
                    options=edge_options)

        self.driver.maximize_window()
        return self.driver

    def close_driver(self):
        if self.driver is not None:
            self.driver.close()
            self.driver = None
