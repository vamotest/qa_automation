import requests
import pytest
from variables import breweries_url


@pytest.fixture()
def response_brewery_list():
    """
    Фикстура возвращает результат запроса получения списка пивоварен
    """
    response = requests.get(breweries_url).json()
    return response


@pytest.fixture()
def state_url():
    """
    Фикстура возвращает ссылку пивоварен по штату
    """
    state_url = f'{breweries_url}' + '?by_state='
    return state_url


@pytest.fixture()
def name_url():
    """
    Фикстура возвращает ссылку пивоварен по имени
    """
    state_url = f'{breweries_url}' + '?by_name='
    return state_url


@pytest.fixture(params=[{"by_tag": "patio"}])
def response_brewery_by_tag(request):
    """
    Фикстура возвращает список пивоварен, выбранных по тегу
    """
    response = requests.get(breweries_url, params=request.param).json()
    return response

