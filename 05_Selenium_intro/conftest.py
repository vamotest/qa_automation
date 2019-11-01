import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        help="This is request browser",
        required=False
    )

    parser.addoption(
        "--opencart_url",
        action="store",
        default="http://localhost:80/",
        help="This is opencart_url",
        required=False
    )


@pytest.fixture()
def browser_param(request):
    return request.config.getoption("--browser")


@pytest.fixture()
def opencart_url_param(request):
    return request.config.getoption('--opencart_url')


@pytest.fixture()
def chosen_driver(browser_param):
    if browser_param == "Chrome":
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")
        driver = webdriver.Chrome(options=options)
        driver.maximize_window()
        return driver
    elif browser_param == "Firefox":
        options = webdriver.FirefoxOptions()
        options.add_argument("--headless")
        driver = webdriver.Firefox(options=options)
        driver.maximize_window()
        return driver
    elif browser_param == "Safari":
        """
        У Safari нет headless-режима
        """
        driver = webdriver.Safari()
        driver.maximize_window()
        return driver


@pytest.fixture()
def opencart_url(opencart_url_param):
    return opencart_url_param
