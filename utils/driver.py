from selenium import webdriver

from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.edge.options import Options as EdgeOptions

from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

from utils.config_reader import ConfigReader


class Driver:
    driver = None

    @staticmethod
    def get_driver() -> webdriver:
        browser = ConfigReader().get_value("selenium", "browser")

        if Driver.driver is None:
            if browser == "firefox":
                firefox_options = FirefoxOptions()
                firefox_options.add_argument("--detach")

                Driver.driver = webdriver.Firefox(
                    executable_path=GeckoDriverManager().install(),
                    options=firefox_options)

            elif browser == "chrome":
                chrome_options = ChromeOptions()
                chrome_options.add_argument("--detach")

                Driver.driver = webdriver.Firefox(
                    executable_path=ChromeDriverManager().install(),
                    options=chrome_options)

            elif browser == "edge":
                edge_options = EdgeOptions()
                edge_options.add_argument("--detach")

                Driver.driver = webdriver.Edge(
                    executable_path=EdgeChromiumDriverManager().install(),
                    options=edge_options)

        Driver.driver.maximize_window()
        return Driver.driver

    @staticmethod
    def close_driver():
        if Driver.driver is not None:
            Driver.driver.close()
            Driver.driver = None
