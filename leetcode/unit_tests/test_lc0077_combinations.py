import unittest
from leetcode.problems.lc0077_combinations import LC0077_Combinations


class LC0077_Combinations_Tests(unittest.TestCase):

    def test_LC0077_Combinations_01(self):
        lc = LC0077_Combinations()

        actual = lc.combine(4, 2)
        expected = [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]

        self.assertEqual(expected, actual)

    def test_LC0077_Combinations_02(self):
        lc = LC0077_Combinations()

        actual = lc.combine(1, 1)
        expected = [[1]]

        self.assertEqual(expected, actual)
