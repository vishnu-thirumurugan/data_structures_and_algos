# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        odd = head
        even = head.next

        oddHead = odd
        evenHead = even

        # create odd list and even list and solve them
        while even and even.next:
            odd.next = even.next # link odd and 3rd odd
            odd = odd.next       # 3rd node as new odd

            even.next = odd.next # connect 0nd and 2nd
            even = even.next     # 2nd as new even 

        # connect odd list with even list
        odd.next = evenHead

        return oddHead







        