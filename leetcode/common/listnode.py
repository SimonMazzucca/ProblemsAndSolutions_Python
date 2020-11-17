class ListNode:
    def __init__(self, val=0, n=None):
        self.val = val
        self.next = n

    def toList(self):
        if self is None:
            return []

        res = [self.val]

        n = self.next
        while n is not None:
            res.append(n.val)
            n = n.next

        return res