from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

class BaseSteps:
    ELEMENT_NOT_EXIST_MESSAGE = "element {} should be present"

    def __init__(self, driver):
        self.driver = driver

    def check_element_exist(self, xpath_locator):
        try:
            self.driver.find_element(By.XPATH, xpath_locator)
        except NoSuchElementException:
            return False
        return True

