import unittest
from leetcode.problems.lc0001_two_sum import LC0001_Two_Sum


class LC0001_Two_Sum_Tests(unittest.TestCase):

    def test_LC0001_Two_Sum_Test_Case_01(self):
        lc = LC0001_Two_Sum()
        nums = [2, 7, 11, 15]
        expected = [0, 1]
        actual = lc.twoSum(nums, 9)

        self.assertEqual(expected, actual)

    def test_LC0001_Two_Sum_Test_Case_02(self):
        lc = LC0001_Two_Sum()
        nums = [3, 2, 4]
        expected = [1, 2]
        actual = lc.twoSum(nums, 6)

        self.assertEqual(expected, actual)

    def test_LC0001_Two_Sum_Test_Case_03(self):
        lc = LC0001_Two_Sum()
        nums = [3, 3]
        expected = [0, 1]
        actual = lc.twoSum(nums, 6)

        self.assertEqual(expected, actual)
