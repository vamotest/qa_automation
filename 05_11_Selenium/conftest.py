from fixtures.browser import Browser
from fixtures.database import DataBase
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
    fixture = Browser(url=url, browser=browser,
                      implicitly_wait=implicitly_wait)
    yield fixture
    fixture.quit()


@pytest.fixture(scope="session")
def database():
    db_config = {
        'host': 'localhost',
        'name': 'bitnami_opencart',
        'user': 'bn_opencart',
        'password': '',
        'port': 3306
    }

    db_fixture = DataBase(
        host=db_config['host'],
        name=db_config['name'],
        user=db_config['user'],
        password=db_config['password'],
        port=db_config['port'])

    yield db_fixture
    db_fixture.destroy()
