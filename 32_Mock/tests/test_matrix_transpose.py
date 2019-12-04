from unittest.mock import patch
import math
from numpy import linalg


def matrix_transpose(matrix):
    det_matrix = math.ceil(linalg.det(matrix))
    return det_matrix


def test_matrix_transpose():
    with patch('builtins.input', side_effect=(-14, 13, -67)):

        assert input() == matrix_transpose(
            [
                [1, 0, -2],
                [3, 2, 1],
                [1, 2, -2]
            ]
        )

        assert input() == matrix_transpose(
            [
                [4, -5, 7],
                [1, -4, 9],
                [-4, 0, 5]
            ]
        )

        assert input() == matrix_transpose(
            [
                [2, 1, 2],
                [0, -1, 3],
                [-6, 5, 4]
            ]
        )
