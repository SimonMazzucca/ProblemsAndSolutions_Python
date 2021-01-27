from leetcode.common.listnode import ListNode


class LC0083_Remove_Duplicates_from_Sorted_List:
    def deleteDuplicates(self, head: ListNode) -> ListNode:

        curr = head
        prev = None

        while curr is not None:

            if prev is not None and curr.val == prev.val:
                prev.next = curr.next

            prev = curr
            curr = curr.next

        return head
