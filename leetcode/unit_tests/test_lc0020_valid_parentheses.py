import unittest
from leetcode.problems.lc0020_valid_parentheses import LC0020_Valid_Parentheses


class LC0020_Valid_Parentheses_Tests(unittest.TestCase):

    def test_LC0020_Valid_Parentheses_01(self):
        lc = LC0020_Valid_Parentheses()
        actual = lc.isValid("()")
        self.assertEqual(True, actual)

    def test_LC0020_Valid_Parentheses_02(self):
        lc = LC0020_Valid_Parentheses()
        actual = lc.isValid("()[]{}")
        self.assertEqual(True, actual)

    def test_LC0020_Valid_Parentheses_03(self):
        lc = LC0020_Valid_Parentheses()
        actual = lc.isValid("(]")
        self.assertEqual(False, actual)

    def test_LC0020_Valid_Parentheses_04(self):
        lc = LC0020_Valid_Parentheses()
        actual = lc.isValid("([)]")
        self.assertEqual(False, actual)

    def test_LC0020_Valid_Parentheses_05(self):
        lc = LC0020_Valid_Parentheses()
        actual = lc.isValid("{[]}")
        self.assertEqual(True, actual)


