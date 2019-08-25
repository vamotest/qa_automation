from python_types import *


class TestPythonExamples:

    def test_start_fixtures(self, module_fixture, session_fixture):
        return module_fixture, session_fixture

    def test_integers(self, sum_integers_data):
        """
        Проверка суммы двух чисел
        :param sum_integers_data:
        :return:
        """

        assert sum_integers(*sum_integers_data) == 9

    def test_string(self, string_data):
        """
        Проверка ялвляется ли числа палиндромом
        :param string_data:
        :return:
        """

        assert string(string_data) == 'YES'


    def test_string_word(self, string_words_data):
        """
        Проверка количества слов в тексте
        :param string_words_data:
        :return:
        """

        assert string_words(string_words_data) == 10


    def test_is_leap(self, is_leap_data):
        """
        Проверка является ли год високосным
        :param is_leap_data:
        :return:
        """

        assert is_leap(is_leap_data) == "YES"


    def test_string_replace(self, string_replace_data):
        """
        Проверка замены строки
        :param string_replace_data:
        :return:
        """

        assert string_replace(string_replace_data) \
            == "one2one3one4one5one6one7one8one9one0one"



    def test_list_matrix_transpose(self, list_data):
        """
        Проверка вычисление определителя матрица
        :param list_data:
        :return:
        """

        determinant = 13
        assert list_matrix_transpose(list_data) == determinant

    def test_list_pairs(self, list_pairs_data):
        """
        Проверка попарных списоков
        :param list_pairs_data:
        :return:
        """
        assert list_pairs(*list_pairs_data) == [(2, -2), (-5, 5),
                                                (6, -6), (-2, 2)]


    def test_set_sym_dif(self, set_data):
        """
        Проверка симметрическая разницы множеств
        :param set_data:
        :return:
        """

        assert set_sym_dif(*set_data) == {1, 2, 3, 7}


    def test_dict_players(self, dict_data):
        """
        Проверка сортировки значений игроков
        :param dict_data:
        :return:
        """

        assert dict_players(**dict_data) == [2780, 2797, 2801, 2822, 2842]

    def test_tuple_text(self, tuple_data):
        """
        Проверка количества вхождений буквы 'а' в текст
        :param tuple_data:
        :return:
        """

        count = 14
        assert tuple_text(tuple_data) == count
