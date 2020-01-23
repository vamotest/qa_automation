from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.admin_page import AdminPage


class Utils:

    def __init__(self, driver):
        self.driver = driver

    def accept_alert(self):
        Alert(self.driver).accept()
        self.wait_success_alert()

    def wait_success_alert(self):
        WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located(
                AdminPage.Products.success_alert
            )
        )
