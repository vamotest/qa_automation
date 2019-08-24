from python_types import sum_integers, string, list_matrix_transpose, \
    list_pairs, set_sym_dif, dict_players, tuple_text, string_words


class TestPythonExamples:

    def test_start_fixtures(self, module_fixture, session_fixture):
        return module_fixture, session_fixture

    def test_integers(self, sum_integers_data):
        """
        Test checks Python data type "Integer"
        :param sum_integers_data:
        :return: sum of two integers
        """

        assert sum_integers(*sum_integers_data) == 9

    def test_string(self, string_data):
        """
        Test checks Python data type "String"
        :param string_data:
        :return: is palindrome string or not
        """

        assert string(string_data) == 'Yes'

    def test_string_word(self, string_words_data):
        """
        :param string_words_data:
        :return:
        """

        assert string_words(string_words_data) == 10


    def test_list_matrix_transpose(self, list_data):
        """
        :param list_data:
        :return:
        """

        determinant = 13
        assert list_matrix_transpose(list_data) == determinant

    def test_list_pairs(self, list_pairs_data):
        """
        :param list_pairs_data:
        :return:
        """
        assert list_pairs(*list_pairs_data) == [(2, -2), (-5, 5),
                                                (6, -6), (-2, 2)]


    def test_set_sym_dif(self, set_data):
        """
        :param set_data:
        :return:
        """

        assert set_sym_dif(*set_data) == {1, 2, 3, 7}


    def test_dict_players(self, dict_data):
        """
        :param dict_data:
        :return:
        """

        assert dict_players(**dict_data) == [2780, 2797, 2801, 2822, 2842]

    def test_tuple_text(self, tuple_data):
        """
        :param tuple_data:
        :return:
        """

        count = 14
        assert tuple_text(tuple_data) == count
