import pytest
from selenium import webdriver


@pytest.fixture
def chrome_browser(request):
    wd = webdriver.Remote("http://localhost:4444/wd/hub", desired_capabilities={'browserName': 'chrome', 'version': '', 'platform': 'ANY'})

    request.addfinalizer(wd.quit)
    return wd


def test_grid(chrome_browser):
    chrome_browser.get("http://www.google.com")
    if not "Google" in chrome_browser.title:
        raise Exception("Unable to load google page!")
    elem = chrome_browser.find_element_by_name("q")
    elem.click()



