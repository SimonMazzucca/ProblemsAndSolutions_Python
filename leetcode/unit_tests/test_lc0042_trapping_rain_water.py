import unittest
from leetcode.problems.lc0042_trapping_rain_water import LC0042_Trapping_Rain_Water


class LC0042_Trapping_Rain_Water_Tests(unittest.TestCase):

    def test_LC0042_Trapping_Rain_Water_01(self):
        lc = LC0042_Trapping_Rain_Water()

        height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
        actual = lc.trap(height)
        self.assertEqual(6, actual)


