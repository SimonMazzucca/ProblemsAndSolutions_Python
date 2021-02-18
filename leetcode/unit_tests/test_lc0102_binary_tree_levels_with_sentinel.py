import unittest
from leetcode.common.treenode import TreeNode
from leetcode.problems.lc0102_binary_tree_levels_with_sentinel import LC0102_Binary_Tree_Levels_with_Sentinel

class LC0102_Binary_Tree_Levels_with_Sentinel_Tests(unittest.TestCase):

    def test_LC0102_Binary_Tree_Levels_with_Sentinel_01(self):
        lc = LC0102_Binary_Tree_Levels_with_Sentinel()

        root = TreeNode.create('3,9,20,null,null,15,7')
        actual = lc.levelOrder(root)
        expected = [
            [3],
            [9, 20],
            [15, 7]
        ]

        self.assertEqual(expected, actual)
