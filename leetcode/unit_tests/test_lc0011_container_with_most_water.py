import unittest
from leetcode.problems.lc0011_container_with_most_water import LC0011_Container_With_Most_Water


class LC0011_Container_With_Most_Water_Tests(unittest.TestCase):

    def test_LC0011_Container_With_Most_Water_01(self):
        lc = LC0011_Container_With_Most_Water()
        height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
        actual = lc.maxArea(height)

        self.assertEqual(49, actual)

