import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

desired_cap = {
 'browser': 'Firefox',
 'browser_version': '70.0 beta',
 'os': 'Windows',
 'os_version': '10',
 'resolution': '2048x1536',
 'name': 'Sample Test'
}

driver = webdriver.Remote(
    command_executor='http://eubelov1:PhgpeViAK8knGySJZPfb@hub.browserstack.com:80/wd/hub',
    desired_capabilities=desired_cap)

driver.maximize_window()
driver.get("http://www.google.com")
if not "Google" in driver.title:
    raise Exception("Unable to load google page!")
elem = driver.find_element_by_name("q")
elem.send_keys("flip a coin")
elem.submit()
print(driver.title)
time.sleep(5)
driver.quit()
