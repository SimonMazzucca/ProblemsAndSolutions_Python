from leetcode.common.listnode import ListNode


class LC0021_Merge_Two_Sorted_Lists:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode()
        res = head

        while l1 is not None and l2 is not None:
            if l1.val <= l2.val:
                res.next = l1
                l1 = l1.next
            else:
                res.next = l2
                l2 = l2.next

            res = res.next

        res.next = l2 if l1 is None else l1

        return head.next
