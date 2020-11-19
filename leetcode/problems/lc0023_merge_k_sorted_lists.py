import queue

from leetcode.common.listnode import ListNode

class LC0023_Merge_k_Sorted_Lists(object):
    def mergeKLists(self, lists):
        k = len(lists)
        q = queue.PriorityQueue(maxsize=k)
        head = ListNode(None)
        curr = head

        for list_idx, node in enumerate(lists):
            if node:
                q.put((node.val, list_idx, node))

        while q.qsize() > 0:
            popped = q.get()
            curr.next, list_idx = popped[2], popped[1]
            curr = curr.next
            if curr.next:
                q.put((curr.next.val, list_idx, curr.next))

        return head.next

    """
    LeetCode solution does not work
    Error: TypeError: '<' not supported between instances of 'ListNode' and 'ListNode'
    Because ListNodes are not comparable
    """
    def mergeKLists_LC(self, lists):
        head = point = ListNode(0)
        q = queue.PriorityQueue()
        for l in lists:
            if l:
                q.put((l.val, l))
        while not q.empty():
            val, node = q.get()
            point.next = ListNode(val)
            point = point.next
            node = node.next
            if node:
                q.put((node.val, node))

        return head.next
