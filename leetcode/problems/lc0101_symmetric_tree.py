from leetcode.common.treenode import TreeNode


class LC0101_Symmetric_Tree:
    def isSymmetric(self, root: TreeNode) -> bool:
        return self.isMirror(root, root)

    def isMirror(self, left, right):
        if left is None and right is None:
            return True
        elif left is None or right is None:
            return False

        if left.val != right.val:
            return False

        return self.isMirror(left.left, right.right) and self.isMirror(left.right, right.left)
