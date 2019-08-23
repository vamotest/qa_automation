from python_types import sum_integers, string


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
