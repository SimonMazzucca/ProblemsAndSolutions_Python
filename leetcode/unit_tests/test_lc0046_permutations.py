import unittest
from leetcode.problems.lc0046_permutations import LC0046_Permutations


class LC0046_Permutations_Tests(unittest.TestCase):

    def test_LC0046_Permutations_01(self):
        lc = LC0046_Permutations()

        actual = lc.permute([1, 2, 3])
        expected = [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]

        self.assertEqual(expected, actual)
