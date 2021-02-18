from leetcode.common.treenode import TreeNode
from typing import List


class LC0102_Binary_Tree_Levels_with_Sentinel:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:

        res = []
        bfs = [root, None]
        level = []

        while len(bfs) > 0:

            node = bfs.pop(0)

            if node is not None:
                level.append(node.val)
                if node.left is not None:
                    bfs.append(node.left)
                if node.right is not None:
                    bfs.append(node.right)
            elif len(level) > 0:
                res.append(level)
                level = []
                bfs.append(None)

        return res
