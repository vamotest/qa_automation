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


@pytest.fixture(scope="session")
def browser(request):
    url = request.config.getoption("--url")
    browser = request.config.getoption("--browser")
    fixture = Browser(url=url, browser=browser)
    yield fixture
    fixture.quit()
