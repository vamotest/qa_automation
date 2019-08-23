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


def list_matrix_transpose(matrix):
    det_matrix = linalg.det(matrix)
    det_matrix = math.ceil(det_matrix)
    return det_matrix
