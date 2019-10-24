def test_firefox_browser(firefox_browser):
    firefox_browser.get("http://www.google.com")
    if "Google" not in firefox_browser.title:
        raise Exception("Unable to load google page!")
    elem = firefox_browser.find_element_by_name("q")
    elem.click()


def test_chrome_browser(chrome_browser):
    chrome_browser.get("http://www.google.com")
    if "Google" not in chrome_browser.title:
        raise Exception("Unable to load google page!")
    elem = chrome_browser.find_element_by_name("q")
    elem.click()
