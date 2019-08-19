import python_types


class TestPythonExamples:

    def test_start_fixtures(self, module_fixture, session_fixture):
        return module_fixture, session_fixture

    def test_integers(self, sum_integers_data):
        """
        Test checks Python data type "integer"
        :param sum_integers_data:
        :return: sum of two integers
        """

        assert sum_integers(*sum_integers_data) == 9