import unittest
from leetcode.problems.lc0054_spiral_matrix import LC0054_Spiral_Matrix


class LC0054_Spiral_Matrix_Tests(unittest.TestCase):

    def test_LC0054_Spiral_Matrix_01(self):
        lc = LC0054_Spiral_Matrix()

        matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        actual = lc.spiralOrder(matrix)
        expected = [1, 2, 3, 6, 9, 8, 7, 4, 5]

        self.assertEqual(expected, actual)

    def test_LC0054_Spiral_Matrix_02(self):
        lc = LC0054_Spiral_Matrix()

        matrix = [[1, 2], [4, 5]]
        actual = lc.spiralOrder(matrix)
        expected = [1, 2, 5, 4]

        self.assertEqual(expected, actual)

    def test_LC0054_Spiral_Matrix_03(self):
        lc = LC0054_Spiral_Matrix()

        matrix = [[]]
        actual = lc.spiralOrder(matrix)
        expected = []

        self.assertEqual(expected, actual)

    def test_LC0054_Spiral_Matrix_04(self):
        lc = LC0054_Spiral_Matrix()

        matrix = [[42]]
        actual = lc.spiralOrder(matrix)
        expected = [42]

        self.assertEqual(expected, actual)
