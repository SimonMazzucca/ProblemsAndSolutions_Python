import unittest
from leetcode.problems.lc0091_decode_ways import LC0091_Decode_Ways


class LC0091_Decode_Ways_Tests(unittest.TestCase):

    def test_LC0091_Decode_Ways_01(self):
        lc = LC0091_Decode_Ways()

        actual = lc.numDecodings('12')
        self.assertEqual(2, actual)

    def test_LC0091_Decode_Ways_02(self):
        lc = LC0091_Decode_Ways()

        actual = lc.numDecodings('226')
        self.assertEqual(3, actual)

    def test_LC0091_Decode_Ways_03(self):
        lc = LC0091_Decode_Ways()

        actual = lc.numDecodings('2222')
        self.assertEqual(5, actual)

    def test_LC0091_Decode_Ways_04(self):
        lc = LC0091_Decode_Ways()

        actual = lc.numDecodings('9999')
        self.assertEqual(1, actual)

    def test_LC0091_Decode_Ways_05(self):
        lc = LC0091_Decode_Ways()

        actual = lc.numDecodings('0')
        self.assertEqual(0, actual)

    def test_LC0091_Decode_Ways_06(self):
        lc = LC0091_Decode_Ways()

        actual = lc.numDecodings('10')
        self.assertEqual(1, actual)

    def test_LC0091_Decode_Ways_07(self):
        lc = LC0091_Decode_Ways()

        actual = lc.numDecodings('00')
        self.assertEqual(0, actual)

    def test_LC0091_Decode_Ways_08(self):
        lc = LC0091_Decode_Ways()

        actual = lc.numDecodings('2101')
        self.assertEqual(1, actual)

    def test_LC0091_Decode_Ways_09(self):
        lc = LC0091_Decode_Ways()

        actual = lc.numDecodings('101')
        self.assertEqual(1, actual)


