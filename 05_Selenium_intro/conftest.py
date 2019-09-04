from selenium import webdriver
import time

chrome = webdriver.Chrome(executable_path='/usr/local/bin/chromedriver')
chrome.get("https://yandex.ru/")
time.sleep(1)
chrome.quit()

firefox = webdriver.Firefox(executable_path='/usr/local/bin/geckodriver')
firefox.get("https://yandex.ru/")
time.sleep(1)
firefox.quit()


safari = webdriver.Safari(executable_path='/usr/bin/safaridriver')
safari.get("https://yandex.ru/")
time.sleep(1)
safari.quit()

