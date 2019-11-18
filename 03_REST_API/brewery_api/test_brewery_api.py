import pytest
import requests
from variables import breweries_url


class TestBrewery:

    def test_brewery_list_not_empty(self, response_brewery_list):
        """
        Тест проверяет, что пришел список пивоварен
        """
        if response_brewery_list is not None:
            print(response_brewery_list)
        elif response_brewery_list is not None:
            assert False, response_brewery_list
        else:
            assert False, 'Something wrong'

    @pytest.mark.parametrize('state', ["Alabama", "Alaska", "Arkansas"])
    def test_brewery_by_state(self, state, state_url):
        """
        Тест проверяет по выбранному штату
        """
        response_brewery_state = requests.get(state_url).json()
        if state in response_brewery_state[0]['state']:
            print(f'State: {state}')
        elif state not in response_brewery_state[0]['state']:
            assert False, f'State: {state}'
        else:
            assert False, 'Something wrong'

    @pytest.mark.parametrize('name', [
        "Trim Tab Brewing", "Yellowhammer Brewery", "Mudshark Brewing Co"])
    def test_brewery_by_name(self, name):
        """
        Тест проверяет по выбранному имени пивоварни
        """
        response_brewery_name = requests.get(breweries_url).json()
        if name in response_brewery_name[0]['name']:
            print(f'Name: {name}')
        elif name not in response_brewery_name[0]['name']:
            assert False, f'Name: {name}'
        else:
            assert False, 'Something wrong'

    @pytest.mark.parametrize('city', [
        "Tucson", "Lake Havasu City", "Chandler", "Phoenix", "Paragould"])
    def test_brewery_by_city(self, city):
        """
        Тест проверяет по выбранному городу
        """
        response_brewery_city = requests.get(breweries_url).json()
        if city in response_brewery_city[0]['city']:
            print(f'City: {city}')
        elif city not in response_brewery_city[0]['city']:
            assert False, f'City: {city}'
        else:
            assert False, 'Something wrong'

    @pytest.mark.parametrize('tag', ["Patio"])
    def test_brewery_by_tag(self, tag, response_brewery_by_tag):
        """
        Тест проверяет по выбранному тегу
        """
        if tag in response_brewery_by_tag[0]['tag_list']:
            print(f'Tag: {tag}')
        elif tag not in response_brewery_by_tag[0]['tag_list']:
            assert False, f'Tag: {tag}'
        else:
            assert False, 'Something wrong'