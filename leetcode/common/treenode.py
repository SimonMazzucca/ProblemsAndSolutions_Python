class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    @staticmethod
    def create(data):
        nodes = data.split(',')

        if nodes[0] is None or nodes[0] == '':
            return None

        root = TreeNode(nodes[0])
        current = root
        queue = []
        left = True

        for i in range(1, len(nodes)):
            if len(queue) > 0 and left:
                current = queue.pop(0)

            if nodes[i] != 'null':

                if left:
                    current.left = TreeNode(nodes[i])
                    queue.append(current.left)
                else:
                    current.right = TreeNode(nodes[i])
                    queue.append(current.right)

            left = not left

        return root
