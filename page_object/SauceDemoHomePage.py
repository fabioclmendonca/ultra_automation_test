from seleniumpagefactory.Pagefactory import PageFactory


class SauceDemoHome(PageFactory):

    def __init__(self, driver):
        self.driver = driver

    locators = {
        "user_name_input": ("ID", "user-name"),
        "password_input": ("ID", "password"),
        "login_button": ("XPATH", "//input[@data-test='login-button']"),
    }

    def click_sign_in(self):
        self.sign_in.click()

    def set_username(self, username):
        self.user_name_input.set_text(username)

    def set_password(self, password):
        self.password_input.set_text(password)

    def click_login_button(self):
        self.login_button.click()
