from locators.user_login import UserLogin as user_login


class UserLogin:

    def __init__(self, driver):
        self.driver = driver

    def fill_username(self, email):
        field = self.driver.find_element(*user_login.email)
        field.clear()
        field.send_keys(email)

    def fill_password(self, password):
        field = self.driver.find_element(*user_login.password)
        field.clear()
        field.send_keys(password)

    def login(self):
        button = self.driver.find_element(*user_login.login_button)
        button.click()
