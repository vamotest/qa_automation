from selenium import webdriver
from .logger import create_log


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
        self.log = create_log()

    def open_main_page(self):
        self.log.info('Opening main page')
        self.wd.get(self.url)

    def open_admin_page(self):
        self.log.info('Opening admin page')
        self.wd.get(self.url + '/admin')

    def quit(self):
        self.log.info('Closing browser')
        self.wd.quit()
