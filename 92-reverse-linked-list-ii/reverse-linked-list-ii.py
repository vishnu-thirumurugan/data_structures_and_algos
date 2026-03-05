# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head

        prev = dummy 
        for _ in range(left-1):
            prev = prev.next

        curr = prev.next  # node where index = left
        for _ in range(right-left):
            # remove the node after left index and add it after prev
            # repeat this process until you go to right
            temp = curr.next 
            curr.next = temp.next
            temp.next = prev.next
            prev.next = temp

        return dummy.next




        