import unittest
from leetcode.problems.lc0067_add_binary import LC0067_Add_Binary


class LC0067_Add_Binary_Tests(unittest.TestCase):

    def test_LC0067_Add_Binary_01(self):
        lc = LC0067_Add_Binary()

        actual = lc.addBinary('11', '1')
        self.assertEqual('100', actual)


    def test_LC0067_Add_Binary_02(self):
        lc = LC0067_Add_Binary()

        actual = lc.addBinary('1', '11')
        self.assertEqual('100', actual)


    def test_LC0067_Add_Binary_03(self):
        lc = LC0067_Add_Binary()

        actual = lc.addBinary('1010', '1011')
        self.assertEqual('10101', actual)


