import pytest
import yaml
from selenium.webdriver.common import desired_capabilities
from selenium import webdriver


conf = yaml.safe_load(open('configuration.yml'))


@pytest.fixture
def firefox_browser(request):
    selenium_grid_url = conf['selenium']['grid_url']
    capabilities = desired_capabilities.DesiredCapabilities.FIREFOX.copy()
    capabilities['browserName'] = "firefox"
    capabilities['version'] = "69"
    capabilities['platform'] = "ANY"
    print(capabilities)
    wd = webdriver.Remote(
        desired_capabilities=capabilities,
        command_executor=selenium_grid_url
    )
    request.addfinalizer(wd.quit)
    return wd


@pytest.fixture
def chrome_browser(request):
    selenium_grid_url = conf['selenium']['grid_url']
    capabilities = desired_capabilities.DesiredCapabilities.CHROME.copy()
    capabilities['browserName'] = "chrome"
    capabilities['version'] = "77"
    capabilities['platform'] = "ANY"
    print(capabilities)
    wd = webdriver.Remote(
        desired_capabilities=capabilities,
        command_executor=selenium_grid_url
    )
    request.addfinalizer(wd.quit)
    return wd
