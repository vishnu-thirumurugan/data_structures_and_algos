# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # reverse the linklist
        # keep track of  largest number
        def reverse(head):
            prev = None
            curr = head 
            while curr:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp

            return prev
        
        head = reverse(head)

        maxVal = head.val
        curr = head
        while curr and curr.next:
            if curr.next.val < maxVal:
                # remove
                curr.next = curr.next.next
            else:
                # update max val
                maxVal = curr.next.val
                curr = curr.next

        return reverse(head)
        