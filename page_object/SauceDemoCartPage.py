from seleniumpagefactory.Pagefactory import PageFactory


class SauceDemoCartPage(PageFactory):

    def __init__(self, driver):
        self.driver = driver

    locators = {
        "checkout_button": ("ID", "checkout"),
    }

    def click_checkout_button(self):
        self.checkout_button.click()
