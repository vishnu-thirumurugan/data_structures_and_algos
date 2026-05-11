# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        smallDummy = ListNode(0)
        largeDummy = ListNode(0)

        small = smallDummy
        large = largeDummy

        curr = head

        while curr:
            if curr.val < x:
                small.next = ListNode(curr.val)
                small = small.next
            else:
                large.next = ListNode(curr.val)
                large = large.next

            curr = curr.next

        large.next = None

        small.next = largeDummy.next

        return smallDummy.next

        
        