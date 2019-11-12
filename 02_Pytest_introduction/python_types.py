import math
from numpy import linalg


def sum_integers(int1, int2):
    # type: (int, int) -> int
    return int1 + int2


def is_leap(year):
    # type: (int) -> str
    return 'YES' if year % 400 == 0 or year % 4 == 0 and not year % 100 == 0 \
        else 'NO'


def string(str_pal):
    # type: (str) -> str
    str_pal_copy = str_pal[:]
    str_pal_copy = str_pal_copy.replace(' ', '')
    str_pal_copy = str_pal_copy.lower()
    return 'YES' if str_pal_copy == str_pal_copy[::-1] else 'NO'


def string_words(text):
    # type: (str) -> int
    words = (text.count(' ') + 1)
    return words


def string_replace(str_for_replace):
    # type: (str) -> str
    replaced = str_for_replace.replace('1', 'one')
    return replaced


def list_matrix_transpose(matrix):
    # type: (list) -> float
    det_matrix = linalg.det(matrix)
    det_matrix = math.ceil(det_matrix)
    return det_matrix


def list_pairs(list1, list2):
    # type: (list, list) -> list
    pairs = []
    for var_x in list1:
        for var_y in list2:
            cur_sum = var_x + var_y
            if cur_sum == 0:
                pairs.append((var_x, var_y))
    return pairs


def set_sym_dif(set1, set2):
    # type: (set, set) -> set
    sym_dif = set1.symmetric_difference(set2)
    return sym_dif


def dict_players(**players):
    # type: (dict) -> list
    values = list(players.values())
    values = sorted(values)
    return values


def tuple_text(text):
    # type: (tuple) -> int
    count_text = text.count('a')
    return count_text
