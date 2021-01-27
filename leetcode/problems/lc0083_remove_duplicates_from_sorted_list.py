from leetcode.common.listnode import ListNode


class LC0083_Remove_Duplicates_from_Sorted_List:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        curr = head

        while curr is not None and curr.next is not None:

            if curr.next.val == curr.val:
                curr.next = curr.next.next
            else:
                curr = curr.next

        return head
