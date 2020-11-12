import unittest
from leetcode.problems.lc0013_roman_to_integer import LC0013_Roman_to_Integer


class LC0013_Roman_to_Integer_Tests(unittest.TestCase):

    def test_LC0013_Roman_to_Integer_01(self):
        lc = LC0013_Roman_to_Integer()
        actual = lc.romanToInt("MCMXCIV")

        self.assertEqual(1994, actual)

