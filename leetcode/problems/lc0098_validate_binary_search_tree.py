from leetcode.common.treenode import TreeNode


class LC0098_Validate_Binary_Search_Tree:
    def isValidBST(self, root: TreeNode) -> bool:
        return self.isValid(root, None, None)

    def isValid(self, root: TreeNode, min: int=None, max: int=None) -> bool:
        if root is None:
            return True

        if min is not None and root.val <= min:
            return False

        if max is not None and root.val >= max:
            return False

        valid = self.isValid(root.left, min, root.val) and self.isValid(root.right, root.val, max)

        return valid
