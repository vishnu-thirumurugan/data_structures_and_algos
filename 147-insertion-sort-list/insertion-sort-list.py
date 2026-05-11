# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)  # sorted
        curr = head          # unsorted

        while curr:
            # keep the next node as temp
            nxt = curr.next

            # move to the point of insertion
            prev = dummy
            while prev.next and prev.next.val < curr.val:
                prev = prev.next

            # insert the node
            curr.next = prev.next
            prev.next = curr

            # set the curr to next in unsorted
            curr = nxt

        return dummy.next
            
        