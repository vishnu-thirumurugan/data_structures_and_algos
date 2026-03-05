# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if not head:
            return head

        dummy = ListNode(-1)
        dummy.next = head
        prev = dummy 
        curr = dummy.next

        while curr:
            if curr.val == val:
                prev.next = prev.next.next
                curr = curr.next
            else:
                prev = curr
                curr = curr.next

        return dummy.next
        