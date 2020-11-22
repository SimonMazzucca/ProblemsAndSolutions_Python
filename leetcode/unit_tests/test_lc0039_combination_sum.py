import unittest
from leetcode.problems.lc0039_combination_sum import LC0039_Combination_Sum


class LC0039_Combination_Sum_Tests(unittest.TestCase):

    def test_LC0039_Combination_Sum_01(self):
        lc = LC0039_Combination_Sum()
        actual = lc.combinationSum([2, 3, 6, 7], 7)
        expected = [
            [2, 2, 3],
            [7]
        ]
        self.assertEqual(expected, actual)

    def test_LC0039_Combination_Sum_01(self):
        lc = LC0039_Combination_Sum()
        actual = lc.combinationSum([2, 3, 5], 8)
        expected = [
            [2, 2, 2, 2],
            [2, 3, 3],
            [3, 5]
        ]
        self.assertEqual(expected, actual)

