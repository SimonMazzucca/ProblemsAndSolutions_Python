import unittest
from leetcode.problems.lc0005_longest_palindromic_substring import LC0005_Longest_Palindromic_Substring


class LC0005_Longest_Palindromic_Substring_Tests(unittest.TestCase):

    def test_LC0005_Longest_Palindromic_Substring_01(self):
        lc = LC0005_Longest_Palindromic_Substring()
        actual = lc.longestPalindrome("babax")

        self.assertEqual("aba", actual)

