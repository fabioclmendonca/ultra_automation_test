import os

from dotenv import load_dotenv
from config.DriverFactory import get_driver
from step_definition.TestSauceDemoSteps import TestSauceDemoSteps


class TestSauceDemo:

    def setup(self):
        load_dotenv()
        self.driver = get_driver(os.getenv('browser'))
        self.sauce_demo_steps = TestSauceDemoSteps(self.driver)
        self.driver.get(os.getenv('base_url'))

    def teardown(self):
        self.driver.quit()

    def test_purchase_flow(self):
        self.sauce_demo_steps.login("standard_user", "secret_sauce")
        self.sauce_demo_steps.click_add_backpack_cart()
        self.sauce_demo_steps.click_cart_button()
        self.sauce_demo_steps.click_checkout_button()
        self.sauce_demo_steps.fill_user_information_and_continue()
        self.sauce_demo_steps.review_and_finish_order()
        self.sauce_demo_steps.check_success_order_header("THANK YOU FOR YOUR ORDER")
        self.sauce_demo_steps.check_success_order_message("Your order has been dispatched, and will arrive just as fast as the pony can get there!")

