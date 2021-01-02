import unittest
from leetcode.problems.lc0050_pow import LC0050_Pow


class LC0050_Pow_Tests(unittest.TestCase):

    def test_LC0050_Pow_01(self):
        lc = LC0050_Pow()
        actual = lc.myPow(2, 10)
        self.assertEqual(1024, actual)

    def test_LC0050_Pow_02(self):
        lc = LC0050_Pow()
        actual = lc.myPow(10, 0)
        self.assertEqual(1, actual)

    def test_LC0050_Pow_03(self):
        lc = LC0050_Pow()
        actual = lc.myPow(2.1, 3)
        self.assertEqual(9.261000000000001, actual)

    def test_LC0050_Pow_04(self):
        lc = LC0050_Pow()
        actual = lc.myPow(2, -2)
        self.assertEqual(.25, actual)

    def test_LC0050_Pow_05(self):
        lc = LC0050_Pow()
        actual = lc.myPow(0.00001, 2147483647)
        self.assertEqual(0, actual)


