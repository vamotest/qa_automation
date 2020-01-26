from locators.admin_login import AdminLogin as admin_login


class AdminLogin:

    def __init__(self, driver):
        self.driver = driver

    def fill_username(self, email):
        field = self.driver.find_element(*admin_login.email)
        field.clear()
        field.send_keys(email)

    def fill_password(self, password):
        field = self.driver.find_element(*admin_login.password)
        field.clear()
        field.send_keys(password)

    def login_button(self):
        button = self.driver.find_element(*admin_login.login_button)
        button.click()
