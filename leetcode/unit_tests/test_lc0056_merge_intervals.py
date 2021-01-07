import unittest
from leetcode.problems.lc0056_merge_intervals import LC0056_Merge_Intervals


class LC0056_Merge_Intervals_Tests(unittest.TestCase):

    def test_LC0056_Merge_Intervals_01(self):
        lc = LC0056_Merge_Intervals()

        intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
        expected = [[1, 6], [8, 10], [15, 18]]

        actual = lc.merge(intervals)

        self.assertEqual(expected, actual)

    def test_LC0056_Merge_Intervals_02(self):
        lc = LC0056_Merge_Intervals()

        intervals = [[1, 4], [4, 5]]
        expected = [[1, 5]]

        actual = lc.merge(intervals)

        self.assertEqual(expected, actual)

    def test_LC0056_Merge_Intervals_03(self):
        lc = LC0056_Merge_Intervals()

        intervals = [[1, 3], [2, 11], [8, 10]]
        expected = [[1, 11]]

        actual = lc.merge(intervals)

        self.assertEqual(expected, actual)
