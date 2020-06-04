import math
from numpy import linalg


def addition_of_numbers(int1, int2):
    # type: (int, int) -> int
    return int1 + int2


def is_leap(year):
    # type: (int) -> str
    return 'YES' if year % 400 == 0 or year % 4 == 0 and not year % 100 == 0 \
        else 'NO'


def is_palindrome(str_pal):
    # type: (str) -> str
    str_pal_copy = str_pal[:]
    str_pal_copy = str_pal_copy.replace(' ', '')
    str_pal_copy = str_pal_copy.lower()
    return 'YES' if str_pal_copy == str_pal_copy[::-1] else 'NO'


def count_words(text):
    # type: (str) -> int
    words = (text.count(' ') + 1)
    return words


def replace_string(str_for_replace):
    # type: (str) -> str
    replaced = str_for_replace.replace('1', 'one')
    return replaced


def transpose_matrix(matrix):
    # type: (list) -> float
    det_matrix = linalg.det(matrix)
    det_matrix = math.ceil(det_matrix)
    return det_matrix


def compare_lists(list1, list2):
    # type: (list, list) -> list
    pairs = []
    for var_x in list1:
        for var_y in list2:
            cur_sum = var_x + var_y
            if cur_sum == 0:
                pairs.append((var_x, var_y))
    return pairs


def find_symmetrical_difference(set1, set2):
    # type: (set, set) -> set
    sym_dif = set1.symmetric_difference(set2)
    return sym_dif


def sort_players_score(**players):
    # type: (dict) -> list
    values = list(players.values())
    values = sorted(values)
    return values


def entry_letter(text):
    # type: (tuple) -> int
    count_text = text.count('a')
    return count_text
