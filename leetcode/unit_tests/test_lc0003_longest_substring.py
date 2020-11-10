import unittest
from leetcode.problems.lc0003_longest_substring import LC0003_Longest_Substring_Without_Repeating_Characters


class LC0003_Longest_Substring_Without_Repeating_Characters_Tests(unittest.TestCase):

    def test_LC0003_Longest_Substring_Tests_01(self):
        lc = LC0003_Longest_Substring_Without_Repeating_Characters()
        actual = lc.lengthOfLongestSubstring("abcabcbb")

        self.assertEqual(3, actual)

    def test_LC0003_Longest_Substring_Tests_02(self):
        lc = LC0003_Longest_Substring_Without_Repeating_Characters()
        actual = lc.lengthOfLongestSubstring("bbbbb")

        self.assertEqual(1, actual)

    def test_LC0003_Longest_Substring_Tests_03(self):
        lc = LC0003_Longest_Substring_Without_Repeating_Characters()
        actual = lc.lengthOfLongestSubstring("pwwkew")

        self.assertEqual(3, actual)

    def test_LC0003_Longest_Substring_Tests_04(self):
        lc = LC0003_Longest_Substring_Without_Repeating_Characters()
        actual = lc.lengthOfLongestSubstring("")

        self.assertEqual(0, actual)

