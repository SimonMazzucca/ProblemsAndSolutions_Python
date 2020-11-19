import unittest

from leetcode.common.listnode import ListNode
from leetcode.problems.lc0023_merge_k_sorted_lists import LC0023_Merge_k_Sorted_Lists


class LC0023_Merge_k_Sorted_Lists_Tests(unittest.TestCase):

    def test_LC0023_Merge_k_Sorted_Lists_01(self):
        lc = LC0023_Merge_k_Sorted_Lists()

        a3 = ListNode(5)
        a2 = ListNode(4, a3)
        a1 = ListNode(1, a2)

        b3 = ListNode(4)
        b2 = ListNode(3, b3)
        b1 = ListNode(1, b2)

        c2 = ListNode(6)
        c1 = ListNode(2, c2)

        actual = lc.mergeKLists([a1, b1, c1])
        expected = [1, 1, 2, 3, 4, 4, 5, 6]
        self.assertEqual(expected, actual.toList())
