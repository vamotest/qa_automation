import pytest


def pytest_addoption(parser):
    parser.addoption(
        "--url",
        default="https://ya.ru",
        help="This is request url"
    )


@pytest.fixture()
def url_param(request):
    """
    Фикстура возвращает результат запроса аргумента командной строки
    """
    return request.config.getoption("--url")
