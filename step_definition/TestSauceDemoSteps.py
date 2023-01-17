import os
import string
import random
from step_definition.BaseSteps import BaseSteps
from page_object.SauceDemoHomePage import SauceDemoHome
from page_object.SauceDemoShopPage import SauceDemoShopPage
from page_object.SauceDemoCartPage import SauceDemoCartPage
from page_object.SauceDemoCheckoutPage import SauceDemoCheckoutPage


class TestSauceDemoSteps(BaseSteps):

    def __init__(self, driver):
        self.home_page = SauceDemoHome(driver)
        self.shop_page = SauceDemoShopPage(driver)
        self.cart_page = SauceDemoCartPage(driver)
        self.checkout_page = SauceDemoCheckoutPage(driver)
        super().__init__(driver)

    def successfully_login(self):
        self.fill_username(os.getenv("login_user"))
        self.fill_password(os.getenv("login_password"))
        self.click_login_button()

    def login(self, user, password):
        self.fill_username(user)
        self.fill_password(password)
        self.click_login_button()

    def fill_username(self, username):
        self.home_page.set_username(username)

    def fill_password(self, password):
        self.home_page.set_password(password)

    def click_login_button(self):
        self.home_page.click_login_button()

    def click_add_backpack_cart(self):
        self.shop_page.click_add_cart_backpack()

    def click_cart_button(self):
        self.shop_page.click_cart_button()

    def click_checkout_button(self):
        self.cart_page.click_checkout_button()

    def fill_user_information_and_continue(self):
        random_first_name = ''.join(random.choice(string.ascii_letters) for i in range(10))
        random_last_name = ''.join(random.choice(string.ascii_letters) for i in range(10))
        random_zip = ''.join(random.choice(string.digits) for i in range(6))
        self.checkout_page.input_first_name(random_first_name)
        self.checkout_page.input_last_name(random_last_name)
        self.checkout_page.input_zip_code(random_zip)
        self.checkout_page.click_continue_button()

    def review_and_finish_order(self):
        is_item_present = self.check_element_exist(self.checkout_page.get_item_locator("item_cart_label"))
        assert is_item_present, super().ELEMENT_NOT_EXIST_MESSAGE.format("zip item_cart_label")
        is_item_price_present = self.check_element_exist(self.checkout_page.get_item_locator("item_cart_price_label"))
        assert is_item_price_present, "element {} should be present".format("zip item_cart_price_label")
        self.checkout_page.click_finish_button()

    def check_success_order_header(self, header):
        self.checkout_page.get_order_complete_header()

    def check_success_order_message(self, message):
        self.checkout_page.get_order_complete_message()
