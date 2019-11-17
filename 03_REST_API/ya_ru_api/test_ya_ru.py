import requests


def test_status_code(url_param):
    """
    Тест проверяет корректность ответа по заданному аргументу командной строки
    """
    response = requests.get(url_param).status_code
    assert response == 200
    print(response)