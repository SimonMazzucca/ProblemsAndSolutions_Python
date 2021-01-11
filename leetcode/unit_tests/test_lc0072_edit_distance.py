import unittest
from leetcode.problems.lc0072_edit_distance import LC0072_Edit_Distance


class LC0072_Edit_Distance_Tests(unittest.TestCase):

    def test_LC0072_Edit_Distance_01(self):
        lc = LC0072_Edit_Distance()

        actual = lc.minDistance('horse', 'ros')
        self.assertEqual(3, actual)

    def test_LC0072_Edit_Distance_02(self):
        lc = LC0072_Edit_Distance()

        actual = lc.minDistance('intention', 'execution')
        self.assertEqual(5, actual)

    def test_LC0072_Edit_Distance_03(self):
        lc = LC0072_Edit_Distance()

        actual = lc.minDistance('saturday', 'sunday')
        self.assertEqual(3, actual)

    def test_LC0072_Edit_Distance_04(self):
        lc = LC0072_Edit_Distance()

        actual = lc.minDistance('zoologicoarchaeologist', 'zoogeologist')
        self.assertEqual(10, actual)



