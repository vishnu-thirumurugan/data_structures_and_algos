# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        sortList = []
        
        curr = head
        while curr:
            sortList.append(curr.val)
            curr = curr.next
        
        sortList.sort()

        dummy = ListNode(0)
        curr = dummy
        for num in sortList:
            node = ListNode(num)
            curr.next = node
            curr = curr.next

        return dummy.next
            


        