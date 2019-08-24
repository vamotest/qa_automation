from numpy import linalg
import math


def sum_integers(int1, int2):
    # type: (int, int) -> int
    return int1 + int2


def string(str_pal):
    # type: (str) -> str
    str_pal_copy = str_pal[:]
    str_pal_copy = str_pal_copy.replace(' ', '')
    str_pal_copy = str_pal_copy.lower()
    return 'Yes' if str_pal_copy == str_pal_copy[::-1] else 'No'


def string_words(text):
    words = (text.count(' ') + 1)
    return words


def list_matrix_transpose(matrix):
    det_matrix = linalg.det(matrix)
    det_matrix = math.ceil(det_matrix)
    return det_matrix


def list_pairs(list1, list2):
    pairs = []
    for x in list1:
        for y in list2:
            cur_sum = x + y
            if cur_sum == 0:
                pairs.append((x, y))
    return pairs


def set_sym_dif(set1, set2):
    sym_dif = set1.symmetric_difference(set2)
    return sym_dif


def dict_players(**players):
    values = list(players.values())
    values = sorted(values)
    return values


def tuple_text(text):
    count_text = text.count('a')
    return count_text
