import allure
import pytest
import requests
from variables import breweries_url


class TestBrewery:
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.description("Тест проверяет, что пришел список пивоварен")
    def test_brewery_list_not_empty(self, response_brewery_list):
        with allure.step("Проверяю, что список пивоварен не пустой"):
            assert response_brewery_list is not None

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description("Тест проверяет по выбранному штату")
    @pytest.mark.parametrize('state', ["Alabama", "Alaska", "Arkansas"])
    def test_brewery_by_state(self, state, state_url):
        response_brewery_state = requests.get(state_url + f'{state}').json()

        with allure.step(
                "Проверяем, что {state} есть в ответе на запрос в поле state"):
            assert state in response_brewery_state[0]['state']

    @allure.severity(allure.severity_level.NORMAL)
    @allure.description("Тест проверяет по выбранному имени пивоварни")
    @pytest.mark.parametrize('name', [
        "Trim Tab Brewing",
        "Yellowhammer Brewery",
        "Mudshark Brewing Co"
    ])
    def test_brewery_by_name(self, name, name_url):
        response_brewery_name = requests.get(name_url + f'{name}').json()

        with allure.step(
                "Проверяем, что {name} есть в ответе на запрос в поле 'name'"
        ):
            assert name in response_brewery_name[0]['name']

    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.parametrize('brewery_id, phone', [
        ("1", "2516897483"),
        ("50", "9073605104"),
        ("100", "9284422337"),
        ("250", "4796362337"),
        ("500", "6192752215")
    ])
    def test_brewery_by_city(self, brewery_id, phone):
        response_brewery_id = \
            requests.get(breweries_url + f'/{brewery_id}').json()

        with allure.step(
                """
                Проверяем, что {brewery_id} есть в ответе на запрос в поле id.
                Что вы выбранном {brewery_id} есть заданный {phone}
                """
        ):
            assert brewery_id == str(response_brewery_id['id']) and \
                   phone == response_brewery_id['phone']

    @allure.description('Тест проверяет по выбранному тегу')
    @allure.severity(allure.severity_level.TRIVIAL)
    @pytest.mark.parametrize('tag', ["patio"])
    def test_brewery_by_tag(self, tag, response_brewery_by_tag):
        with allure.step("Проверяем, что выбранный тег есть в списке тегов"):
            assert tag in response_brewery_by_tag[0]['tag_list']
