import unittest
from leetcode.problems.lc0048_rotate_image import LC0048_Rotate_Image


class LC0048_Rotate_Image_Tests(unittest.TestCase):

    def test_LC0048_Rotate_Image_01(self):
        lc = LC0048_Rotate_Image()

        matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        expected = [[7, 4, 1], [8, 5, 2], [9, 6, 3]]

        lc.rotate(matrix, 1)
        self.assertEqual(expected, matrix)

        matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        lc.rotate(matrix, 5)
        self.assertEqual(expected, matrix)



    def test_LC0048_Rotate_Image_02(self):
        lc = LC0048_Rotate_Image()

        matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        expected = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]

        lc.rotate(matrix, 2)
        self.assertEqual(expected, matrix)

        matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        lc.rotate(matrix, 6)
        self.assertEqual(expected, matrix)


