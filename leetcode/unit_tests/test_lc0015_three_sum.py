import unittest
from leetcode.problems.lc0015_three_sum import LC0015_Three_Sum


class LC0015_Three_Sum_Tests(unittest.TestCase):

    def test_LC0015_Three_Sum_01(self):
        lc = LC0015_Three_Sum()
        nums = [-1, 0, 1, 2, -1, -4]
        actual = lc.threeSum(nums)
        expected = [
            [-1, -1, 2],
            [-1, 0, 1]
        ]
        self.assertEqual(expected, actual)

    def test_LC0015_Three_Sum_02(self):
        lc = LC0015_Three_Sum()
        nums = []
        actual = lc.threeSum(nums)
        expected = [
        ]
        self.assertEqual(expected, actual)

    def test_LC0015_Three_Sum_03(self):
        lc = LC0015_Three_Sum()
        nums = [0]
        actual = lc.threeSum(nums)
        expected = [
        ]
        self.assertEqual(expected, actual)

    def test_LC0015_Three_Sum_04(self):
        lc = LC0015_Three_Sum()
        nums = [-2, 0, 0, 2, 2]
        actual = lc.threeSum(nums)
        expected = [
            [-2, 0, 2]
        ]
        self.assertEqual(expected, actual)

