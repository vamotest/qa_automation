from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.admin_page import AdminPage


class Browser:

    def __init__(self, browser, url, implicitly_wait):
        if browser.lower() == 'chrome':
            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_argument('headless')
            self.wd = webdriver.Chrome(options=chrome_options)
            self.wd.maximize_window()
        elif browser.lower() == 'firefox':
            firefox_options = webdriver.FirefoxOptions()
            firefox_options.add_argument('headless')
            self.wd = webdriver.Firefox(options=firefox_options)
            self.wd.maximize_window()
        elif browser.lower() == 'safari':
            self.wd = webdriver.Safari()
            self.wd.maximize_window()
        else:
            raise ValueError(f'Unrecognized browser: {browser}')
        self.wd.implicitly_wait(int(implicitly_wait))
        self.url = url

    def open_main_page(self):
        self.wd.get(self.url)

    def open_admin_page(self):
        self.wd.get(self.url + '/admin')

    def accept_alert(self):
        Alert(self.wd).accept()
        WebDriverWait(self.wd, 5).until(
            EC.presence_of_element_located(AdminPage.Products.success_delete))

    def quit(self):
        self.wd.quit()
