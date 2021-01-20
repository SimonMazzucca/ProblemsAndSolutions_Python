import unittest
from leetcode.problems.lc0076_minimum_window_substring import LC0076_Minimum_Window_Substring


class LC0076_Minimum_Window_Substring_Tests(unittest.TestCase):

    def test_LC0076_Minimum_Window_Substring_01(self):
        lc = LC0076_Minimum_Window_Substring()

        actual = lc.minWindow('ADOBECODEBANC', 'ABC')
        self.assertEqual('BANC', actual)

    def test_LC0076_Minimum_Window_Substring_02(self):
        lc = LC0076_Minimum_Window_Substring()

        actual = lc.minWindow('a', 'a')
        self.assertEqual('a', actual)

    def test_LC0076_Minimum_Window_Substring_03(self):
        lc = LC0076_Minimum_Window_Substring()

        actual = lc.minWindow('ab', 'a')
        self.assertEqual('a', actual)

    def test_LC0076_Minimum_Window_Substring_04(self):
        lc = LC0076_Minimum_Window_Substring()

        actual = lc.minWindow('ab', 'b')
        self.assertEqual('b', actual)

    def test_LC0076_Minimum_Window_Substring_05(self):
        lc = LC0076_Minimum_Window_Substring()

        actual = lc.minWindow('abc', 'bc')
        self.assertEqual('bc', actual)


