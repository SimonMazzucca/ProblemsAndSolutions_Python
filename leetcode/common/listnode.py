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

    @staticmethod
    def create(lst=[]):
        if lst is None or lst == []:
            return None

        head = ListNode(lst[0])
        curr = head

        for i in range(1, len(lst)):
            curr.next = ListNode(lst[i])
            curr = curr.next

        return head
