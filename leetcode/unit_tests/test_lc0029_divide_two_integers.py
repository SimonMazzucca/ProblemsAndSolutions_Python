import unittest
from leetcode.problems.lc0029_divide_two_integers import LC0029_Divide_Two_Integers


class LC0029_Divide_Two_Integers_Tests(unittest.TestCase):

    def test_LC0029_Divide_Two_Integers_01(self):
        lc = LC0029_Divide_Two_Integers()

        actual = lc.divide(10, 3)
        self.assertEqual(3, actual)

    def test_LC0029_Divide_Two_Integers_02(self):
        lc = LC0029_Divide_Two_Integers()

        actual = lc.divide(7, -3)
        self.assertEqual(-2, actual)

    def test_LC0029_Divide_Two_Integers_03(self):
        lc = LC0029_Divide_Two_Integers()

        actual = lc.divide(-1, -1)
        self.assertEqual(1, actual)

    def test_LC0029_Divide_Two_Integers_04(self):
        lc = LC0029_Divide_Two_Integers()

        actual = lc.divide(1, 2)
        self.assertEqual(0, actual)

