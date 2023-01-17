from seleniumpagefactory.Pagefactory import PageFactory


class SauceDemoShopPage(PageFactory):

    def __init__(self, driver):
        self.driver = driver

    locators = {
        "add_cart_backpack_button": ("XPATH", "//button[@data-test='add-to-cart-sauce-labs-backpack']"),
        "cart_button": ("XPATH", "//div[@id='shopping_cart_container']/a"),
    }

    def click_add_cart_backpack(self):
        self.add_cart_backpack_button.click()

    def click_cart_button(self):
        self.cart_button.click()
