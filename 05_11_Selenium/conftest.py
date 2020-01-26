from fixtures.browser import Browser
import pytest


def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        help="This is request browser",
        required=False
    )

    parser.addoption(
        "--url",
        action="store",
        default="http://127.0.0.1:80",
        help="This is opencart_url",
        required=False
    )

    parser.addoption(
        "--implicitly_wait",
        action="store",
        default="60",
        help="Implicit browser timeout in seconds",
        required=False
    )


@pytest.fixture(scope="session")
def browser(request):
    url = request.config.getoption("--url")
    browser = request.config.getoption("--browser")
    implicitly_wait = request.config.getoption("--implicitly_wait")
    fixture = Browser(url=url, browser=browser, implicitly_wait=implicitly_wait)
    yield fixture
    fixture.quit()
