from variables import random_image_url, concrete_breed_url, all_breeds_url
import requests
import pytest


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
