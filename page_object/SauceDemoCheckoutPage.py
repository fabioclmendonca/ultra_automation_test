from seleniumpagefactory.Pagefactory import PageFactory


class SauceDemoCheckoutPage(PageFactory):

    def __init__(self, driver):
        self.driver = driver

    locators = {
        "first_name_input": ("ID", "first-name"),
        "last_name_input": ("ID", "last-name"),
        "zip_input": ("ID", "postal-code"),
        "continue_button": ("ID", "continue"),
        "finish_button": ("ID", "finish"),
        "item_cart_label": ("XPATH", "//a[@id='item_4_title_link']/div"),
        "item_cart_price_label": ("XPATH", "//div[@class='inventory_item_price']"),
        "order_complete_header_label": ("XPATH", "//div[@class='checkout_complete_container']/h2"),
        "order_complete_message_label": ("XPATH", "//div[@class='checkout_complete_container']//div"),
    }

    def input_first_name(self, first_name):
        self.first_name_input.set_text(first_name)

    def input_last_name(self, last_name):
        self.last_name_input.set_text(last_name)

    def input_zip_code(self, zip):
        self.zip_input.set_text(zip)

    def click_continue_button(self):
        self.continue_button.click()

    def click_finish_button(self):
        self.finish_button.click()

    def get_item_locator(self, label):
        return self.locators[label][1]

    def get_order_complete_header(self):
        return self.order_complete_header_label.get_text()

    def get_order_complete_message(self):
        return self.order_complete_message_label.get_text()
