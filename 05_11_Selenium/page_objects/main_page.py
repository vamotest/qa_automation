from locators.main_page import MainPage as main_page


class MainPage:

    def __init__(self, driver):
        self.driver = driver

    def search(self, text):

        search_string = self.driver.find_element(*main_page.search_string)
        search_string.clear()
        search_string.send_keys(text)

        search_button = self.driver.find_element(*main_page.search_button)
        search_button.click()

    def switch_next_banner(self):
        next_banner_button = self.driver.find_element(*main_page.next_banner)
        next_banner_button.click()

    def check_banner_is_present(self, banner):
        if banner == 'macbook':
            self.driver.find_element(*main_page.macbook_banner)
        elif banner == 'iphone':
            self.driver.find_element(*main_page.iphone_banner)
