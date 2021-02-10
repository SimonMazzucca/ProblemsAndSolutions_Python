import unittest

from leetcode.common.treenode import TreeNode
from leetcode.problems.lc0101_symmetric_tree import LC0101_Symmetric_Tree


class LC0101_Symmetric_Tree_Tests(unittest.TestCase):

    def test_LC0101_Symmetric_Tree_00(self):
        lc = LC0101_Symmetric_Tree()

        root = TreeNode(1)
        actual = lc.isSymmetric(root)

        self.assertTrue(actual)

    def test_LC0101_Symmetric_Tree_01(self):
        lc = LC0101_Symmetric_Tree()

        root = TreeNode.create('1,2,2,3,4,4,3')
        actual = lc.isSymmetric(root)

        self.assertTrue(actual)

    def test_LC0101_Symmetric_Tree_02(self):
        lc = LC0101_Symmetric_Tree()

        root = TreeNode.create('1,2,2,null,3,null,3')
        actual = lc.isSymmetric(root)

        self.assertFalse(actual)
