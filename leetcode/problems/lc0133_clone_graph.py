# Definition for a Node.
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class LC0133_Clone_Graph:
    def __init__(self):
        self.visited = {}

    def cloneGraph(self, node: 'Node') -> 'Node':

        if node is None:
            return None

        if node in self.visited:
            return self.visited[node]

        clone_node = Node(node.val)

        self.visited[node] = clone_node

        for n in node.neighbors:
            new_n = self.cloneGraph(n)
            clone_node.neighbors.append(new_n)

        # fancy ass version
        # if node.neighbors:
        #     clone_node.neighbors = [self.cloneGraph(n) for n in node.neighbors]

        return clone_node
