import unittest
from leetcode.problems.lc0088_merge_sorted_array import LC0088_Merge_Sorted_Array


class LC0088_Merge_Sorted_Array_Tests(unittest.TestCase):

    def test_LC0088_Merge_Sorted_Array_01(self):
        lc = LC0088_Merge_Sorted_Array()

        nums1 = [1, 2, 3, 0, 0, 0]
        nums2 = [2, 5, 6]
        expected = [1, 2, 2, 3, 5, 6]
        lc.merge(nums1, 3, nums2, 3)

        self.assertEqual(expected, nums1)

    def test_LC0088_Merge_Sorted_Array_02(self):
        lc = LC0088_Merge_Sorted_Array()

        nums1 = [0]
        nums2 = [1]
        expected = [1]
        lc.merge(nums1, 0, nums2, 1)

        self.assertEqual(expected, nums1)

    def test_LC0088_Merge_Sorted_Array_03(self):
        lc = LC0088_Merge_Sorted_Array()

        nums1 = [1, 0]
        nums2 = [0]
        expected = [0, 1]
        lc.merge(nums1, 1, nums2, 1)

        self.assertEqual(expected, nums1)

    def test_LC0088_Merge_Sorted_Array_04(self):
        lc = LC0088_Merge_Sorted_Array()

        nums1 = [4, 5, 6, 0, 0, 0]
        nums2 = [1, 2, 3]
        expected = [1, 2, 3, 4, 5, 6]
        lc.merge(nums1, 3, nums2, 3)

        self.assertEqual(expected, nums1)

