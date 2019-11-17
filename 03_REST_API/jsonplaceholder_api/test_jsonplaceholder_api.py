import pytest
import requests
from variables import json_url


class TestJsonPlaceholder:

    @pytest.mark.parametrize('post_id', [1, 50, 100])
    def test_post_by_id(self, post_id):
        """
        Тест проверяет наличие поста по выбранному id
        """
        result = requests.get(json_url + 'posts' + f'/{post_id}').json()
        assert result['id'] == post_id

    @pytest.mark.parametrize('comment_id', [1, 250, 500])
    def test_comments_by_id(self, comment_id):
        """
        Тест проверяет наличие комментария по выбранному id
        """
        result = requests.get(json_url + 'comments' + f'/{comment_id}').json()
        assert result['id'] == comment_id

    @pytest.mark.parametrize('album_id', [1, 50, 100])
    def test_comments_by_id(self, album_id):
        """
        Тест проверяет наличие альбому по выбранному id
        """
        result = requests.get(json_url + 'albums' + f'/{album_id}').json()
        assert result['id'] == album_id

    @pytest.mark.parametrize('user_id, name', [
        (1, 'Leanne Graham'), (5, 'Chelsey Dietrich'),
        (10, 'Clementina DuBuque')])
    def test_user_id_by_name(self, user_id, name):
        """
        Тест проверяет имя пользователя по выбранному user_id
        """
        result = requests.get(json_url + 'users' + f'/{user_id}').json()
        assert result['name'] == name

    @pytest.mark.parametrize('user_id, lat, lng', [
        (1, '-37.3159', '81.1496'), (5, '-31.8129', '62.5342'),
        (10, '-38.2386', '57.2232')])
    def test_user_id_by_name(self, user_id, lat, lng):
        """
        Тест проверяет координаты пользователя по выбранному user_id
        """
        result = requests.get(json_url + 'users' + f'/{user_id}').json()
        assert result['address']['geo']['lat'] == lat and \
               result['address']['geo']['lng'] == lng
