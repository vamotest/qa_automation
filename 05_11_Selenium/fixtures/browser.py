from .logger import create_log
from utils.sqlite import Sqlite
import datetime
import time
import os

from selenium import webdriver
from selenium.webdriver.support.events import EventFiringWebDriver, AbstractEventListener


class Browser:

    def __init__(self, browser, url, implicitly_wait):
        if browser.lower() == 'chrome':
            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_argument('headless')
            wd = webdriver.Chrome(options=chrome_options)
            self.wd = EventFiringWebDriver(wd, MyListener())
            self.wd.maximize_window()
        elif browser.lower() == 'firefox':
            firefox_options = webdriver.FirefoxOptions()
            firefox_options.add_argument('headless')
            wd = webdriver.Firefox(options=firefox_options)
            self.wd = EventFiringWebDriver(wd, MyListener())
            self.wd.maximize_window()
        elif browser.lower() == 'safari':
            wd = webdriver.Safari()
            self.wd = EventFiringWebDriver(wd, MyListener())
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


class MyListener(AbstractEventListener):

    def __init__(self, *args, **kwargs):
        self.log = create_log()
        super().__init__(*args, **kwargs)
        self.db_log = Sqlite()

    def on_exception(self, exception, driver):

        try:
            os.stat('screenshots')
        except FileNotFoundError:
            os.mkdir('screenshots')

        date = datetime.datetime.now().strftime('%Y-%m-%d')

        self.db_log.write_log(
            f'Screenshot path - screenshots/exception-'
            f'{date}-{time.time()}-{exception}.png')
        driver.save_screenshot(
            f'screenshots/exception-{date}-{time.time()}-{exception}.png')
        print(exception)

    def before_find(self, by, value, driver):
        self.db_log.write_log(f'Finding by - {by}, selector - {value}')
        self.log.info(f'Finding by - {by}, selector - {value}')
        print(by, value)

    def before_click(self, element, driver):
        self.db_log.write_log(f'Clicking on {element}')
        self.log.info(f'Clicking on {element}')
        print(element)
