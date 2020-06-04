from python_types import addition_of_numbers, is_leap, is_palindrome, \
    count_words, replace_string, transpose_matrix, compare_lists, \
    find_symmetrical_difference, sort_players_score, entry_letter


class TestPythonExamples:

    def test_start_fixtures(self, module_fixture, session_fixture):
        return module_fixture, session_fixture

    def test_addition_of_numbers(self, addition_of_numbers_data):
        """
        Проверка суммы двух чисел
        :param addition_of_numbers_data:
        """
        assert addition_of_numbers(*addition_of_numbers_data) == 9

    def test_is_palindrome(self, is_palindrome_data):
        """
        Проверка является ли числа палиндромом
        :param is_palindrome_data:
        """
        assert is_palindrome(is_palindrome_data) == 'YES'

    def test_count_word(self, count_words_data):
        """
        Проверка количества слов в тексте
        :param count_words_data:
        """
        result = count_words(count_words_data)
        assert result == 10

    def test_is_leap(self, is_leap_data):
        """
        Проверка является ли год високосным
        :param is_leap_data:
        """
        result = is_leap(is_leap_data)
        assert result == "YES"

    def test_replace_string(self, replace_string_data):
        """
        Проверка замены строки
        :param replace_string_data:
        """
        result = replace_string(replace_string_data)
        assert result == "one2one3one4one5one6one7one8one9one0one"

    def test_transpose_matrix(self, transpose_matrix_data):
        """
        Проверка вычисление определителя матрицы
        :param transpose_matrix_data:
        """
        determinant = 13
        result = transpose_matrix(transpose_matrix_data)
        assert result == determinant

    def test_compare_lists(self, compare_lists_data):
        """
        Проверка сравнение попарных списков
        :param compare_lists_data:
        """
        result = compare_lists(*compare_lists_data)
        assert result == [(2, -2), (-5, 5), (6, -6), (-2, 2)]

    def test_find_symmetrical_difference(self, find_set_data):
        """
        Проверка симметрическая разницы множеств
        :param find_set_data:
        """
        result = find_symmetrical_difference(*find_set_data)
        assert result == {1, 2, 3, 7}

    def test_dict_players(self, sort_players_score_data):
        """
        Проверка сортировки значений игроков
        :param sort_players_score_data:
        """
        result = sort_players_score(**sort_players_score_data)
        assert result == [2780, 2797, 2801, 2822, 2842]

    def test_entry_letter(self, entry_letter_data):
        """
        Проверка количества вхождений буквы 'а' в текст
        :param entry_letter_data:
        """
        count_letter = 14
        result = entry_letter(entry_letter_data)
        assert result == count_letter
