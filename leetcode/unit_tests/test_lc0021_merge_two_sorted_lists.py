import unittest

from leetcode.common.listnode import ListNode
from leetcode.problems.lc0021_merge_two_sorted_lists import LC0021_Merge_Two_Sorted_Lists


class LC0021_Merge_Two_Sorted_Lists_Tests(unittest.TestCase):

    def test_LC0021_Merge_Two_Sorted_Lists_01(self):
        lc = LC0021_Merge_Two_Sorted_Lists()

        a3 = ListNode(4)
        a2 = ListNode(2, a3)
        a1 = ListNode(1, a2)

        b3 = ListNode(4)
        b2 = ListNode(3, b3)
        b1 = ListNode(1, b2)

        actual = lc.mergeTwoLists(a1, b1)
        expected = [1, 1, 2, 3, 4, 4]
        self.assertEqual(expected, actual.toList())
