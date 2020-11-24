import unittest
from leetcode.problems.lc0041_first_missing_positive import LC0041_First_Missing_Positive


class LC0041_First_Missing_Positive_Tests(unittest.TestCase):

    def test_LC0041_First_Missing_Positive_01(self):
        lc = LC0041_First_Missing_Positive()
        actual = lc.firstMissingPositive([1, 2, 0])
        self.assertEqual(3, actual)

    def test_LC0041_First_Missing_Positive_02(self):
        lc = LC0041_First_Missing_Positive()
        actual = lc.firstMissingPositive([3, 4, -1, 1])
        self.assertEqual(2, actual)

    def test_LC0041_First_Missing_Positive_03(self):
        lc = LC0041_First_Missing_Positive()
        actual = lc.firstMissingPositive([7, 8, 9, 11, 12])
        self.assertEqual(1, actual)

    def test_LC0041_First_Missing_Positive_04(self):
        lc = LC0041_First_Missing_Positive()
        actual = lc.firstMissingPositive([2, 1])
        self.assertEqual(3, actual)



