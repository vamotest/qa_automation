import requests
import pytest

# url произвольного изображения породы собаки
random_image_url = 'https://dog.ceo/api/breeds/image/random'

# url породы собаки
concrete_breed_url = 'https://dog.ceo/api/breed/'

# url списка всех пород
all_breeds_url = 'https://dog.ceo/api/breeds/list/all'


@pytest.fixture()
def response_status():
    """
    Фикстура возвращает статус ответа произвольного изображения собаки
    """
    response = requests.get(random_image_url).json().get("status")
    print(response)
    return response


@pytest.fixture()
def response_status_code():
    """
    Фикстура возвращает код ответа произвольного изображения собаки
    """
    response = requests.get(random_image_url).status_code
    return response


@pytest.fixture()
def response_breeds_list():
    """
    Фикстура возвращает список всех пород собак
    """
    response = requests.get(all_breeds_url).json()
    return response


@pytest.fixture(params=["akita", "eskimo", "vizsla", "whippet"])
def response_status_breed(request):
    """
    Фикстура возвращает статус ответа породы собаки
    """
    response = requests.get(
        concrete_breed_url + f'{request.param}/list'
    ).json()['status']
    return response
