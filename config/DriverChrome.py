import os
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from config.Driver import Driver


class DriverChrome(Driver):

    def get_driver(self):
        chrome_options = self._get_driver_options()
        chrome_desired_capabilities = self._get_capabilities()
        return webdriver.Chrome(ChromeDriverManager().install(),
                                chrome_options=chrome_options,
                                desired_capabilities=chrome_desired_capabilities)

    def _get_driver_options(self):
        chrome_options = Options()
        chrome_options.add_argument("-test-type")
        if os.getenv("headless_browser") == "True":
            chrome_options.add_argument("--headless")
            chrome_options.add_argument("--disable-gpu")
        return chrome_options

    def _get_capabilities(self):
        return DesiredCapabilities.CHROME
