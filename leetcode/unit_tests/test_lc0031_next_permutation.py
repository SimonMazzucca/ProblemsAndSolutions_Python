import unittest
from leetcode.problems.lc0031_next_permutation import LC0031_Next_Permutation


class LC0031_Next_Permutation_Tests(unittest.TestCase):

    def test_LC0031_Next_Permutation_01(self):
        lc = LC0031_Next_Permutation()
        nums = [1, 2, 3]
        lc.nextPermutation(nums)
        expected = [1, 3, 2]
        self.assertEqual(expected, nums)

    def test_LC0031_Next_Permutation_02(self):
        lc = LC0031_Next_Permutation()
        nums = [3, 2, 1]
        lc.nextPermutation(nums)
        expected = [1, 2, 3]
        self.assertEqual(expected, nums)

    def test_LC0031_Next_Permutation_03(self):
        lc = LC0031_Next_Permutation()
        nums = [1, 1, 5]
        lc.nextPermutation(nums)
        expected = [1, 5, 1]
        self.assertEqual(expected, nums)

    def test_LC0031_Next_Permutation_04(self):
        lc = LC0031_Next_Permutation()
        nums = [1, 5, 8, 4, 7, 6, 5, 3, 1]
        lc.nextPermutation(nums)
        expected = [1, 5, 8, 5, 1, 3, 4, 6, 7]
        self.assertEqual(expected, nums)

    def test_LC0031_Next_Permutation_09(self):
        lc = LC0031_Next_Permutation()
        nums = [1]
        lc.nextPermutation(nums)
        expected = [1]
        self.assertEqual(expected, nums)

    def test_LC0031_Next_Permutation_10(self):
        lc = LC0031_Next_Permutation()
        nums = [1, 2]
        lc.nextPermutation(nums)
        expected = [2, 1]
        self.assertEqual(expected, nums)

