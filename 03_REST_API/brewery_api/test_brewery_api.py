import pytest
import requests
from variables import breweries_url


class TestBrewery:

    def test_brewery_list_not_empty(self, response_brewery_list):
        """
        Тест проверяет, что пришел список пивоварен
        """
        assert response_brewery_list is not None

    @pytest.mark.parametrize('state', ["Alabama", "Alaska", "Arkansas"])
    def test_brewery_by_state(self, state, state_url):
        """
        Тест проверяет по выбранному штату
        """
        response_brewery_state = requests.get(state_url + f'{state}').json()

        # Проверяем, что {state} есть в ответе на запрос в поле 'state'
        assert state in response_brewery_state[0]['state']

    @pytest.mark.parametrize('name', [
        "Trim Tab Brewing",
        "Yellowhammer Brewery",
        "Mudshark Brewing Co"
    ])
    def test_brewery_by_name(self, name, name_url):
        """
        Тест проверяет по выбранному имени пивоварни
        """
        response_brewery_name = requests.get(name_url + f'{name}').json()

        # Проверяем, что {name} есть в ответе на запрос в поле 'name'
        assert name in response_brewery_name[0]['name']

    @pytest.mark.parametrize('brewery_id, phone', [
        ("1", "2516897483"),
        ("50", "9073605104"),
        ("100", "9284422337"),
        ("250", "4796362337"),
        ("500", "6192752215")
    ])
    def test_brewery_by_city(self, brewery_id, phone):
        """
        Проверяем, что {brewery_id} есть в ответе на запрос в поле 'id'
        И что вы выбранном {brewery_id} есть заданный {phone}
        """
        response_brewery_id = \
            requests.get(breweries_url + f'/{brewery_id}').json()
        assert \
            brewery_id == str(response_brewery_id['id']) and\
            phone == response_brewery_id['phone']

    @pytest.mark.parametrize('tag', ["patio"])
    def test_brewery_by_tag(self, tag, response_brewery_by_tag):
        """
        Тест проверяет по выбранному тегу
        """
        assert tag in response_brewery_by_tag[0]['tag_list']
