from locators.admin_page import AdminPage as admin_page


class AdminPage:

    def __init__(self, driver):
        self.driver = driver

    def logout(self):
        button = self.driver.find_element(*admin_page.logout)
        button.click()
