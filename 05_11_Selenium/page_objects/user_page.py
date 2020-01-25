from locators.user_page import UserPage as user_page


class UserPage:

    def __init__(self, driver):
        self.driver = driver

    def my_account(self):
        my_account = self.driver.find_element(*user_page.my_account)
        my_account.click()

    def log_in(self):
        log_in = self.driver.find_element(*user_page.log_in)
        log_in.click()

    def log_out(self):
        log_out = self.driver.find_element(*user_page.log_out)
        log_out.click()

    def confirm_exit(self):
        confirm = self.driver.find_element(*user_page.continue_button)
        confirm.click()
