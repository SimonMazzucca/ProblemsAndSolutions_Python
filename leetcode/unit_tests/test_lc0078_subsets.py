import unittest
from leetcode.problems.lc0078_subsets import LC0078_Subsets


class LC0078_Subsets_Tests(unittest.TestCase):

    def test_LC0078_Subsets_01(self):
        lc = LC0078_Subsets()

        actual = lc.subsets([1, 2, 3])
        expected = [
            [],
            [1],
            [2],
            [1, 2],
            [3],
            [1, 3],
            [2, 3],
            [1, 2, 3]
        ]

        self.assertEqual(expected, actual)

