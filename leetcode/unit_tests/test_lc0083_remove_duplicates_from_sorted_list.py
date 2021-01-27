import unittest
from leetcode.problems.lc0083_remove_duplicates_from_sorted_list import LC0083_Remove_Duplicates_from_Sorted_List
from leetcode.common.listnode import ListNode


class LC0083_Remove_Duplicates_from_Sorted_List_Tests(unittest.TestCase):

    def test_LC0083_Remove_Duplicates_from_Sorted_List_01(self):
        lc = LC0083_Remove_Duplicates_from_Sorted_List()

        head = ListNode.create([1, 1, 2])
        actual = lc.deleteDuplicates(head)
        expected = [1, 2]

        self.assertEqual(expected, actual.toList())


    def test_LC0083_Remove_Duplicates_from_Sorted_List_02(self):
        lc = LC0083_Remove_Duplicates_from_Sorted_List()

        head = ListNode.create([1, 1, 2, 3, 3])
        actual = lc.deleteDuplicates(head)
        expected = [1, 2, 3]

        self.assertEqual(expected, actual.toList())


    def test_LC0083_Remove_Duplicates_from_Sorted_List_03(self):
        lc = LC0083_Remove_Duplicates_from_Sorted_List()

        head = None
        actual = lc.deleteDuplicates(head)

        self.assertIsNone(actual)


