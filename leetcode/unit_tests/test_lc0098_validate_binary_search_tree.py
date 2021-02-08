import unittest
from leetcode.problems.lc0098_validate_binary_search_tree import LC0098_Validate_Binary_Search_Tree
from leetcode.common.treenode import TreeNode

class LC0098_Validate_Binary_Search_Tree_Tests(unittest.TestCase):

    def test_LC0098_Validate_Binary_Search_Tree_01(self):
        lc = LC0098_Validate_Binary_Search_Tree()

        root = TreeNode(1)
        root.left = TreeNode(1)

        actual = lc.isValidBST(root)
        self.assertEqual(False, actual)


