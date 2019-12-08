from selenium.webdriver.common.by import By


class UserPage:

    my_account = (By.LINK_TEXT, 'My Account')
    log_in = (By.LINK_TEXT, 'Login')
    log_out = (By.LINK_TEXT, 'Logout')
    continue_button = (By.LINK_TEXT, 'Continue')
