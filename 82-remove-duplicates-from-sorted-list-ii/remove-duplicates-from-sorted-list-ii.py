# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:

        dupList = defaultdict(int)

        curr = head
        while curr:
            dupList[curr.val] += 1
            curr = curr.next

        dummy = ListNode(-101)
        dummy.next = head

        curr = dummy
        while curr and curr.next:
            if dupList[curr.next.val] > 1:
                curr.next = curr.next.next
            else:
                curr = curr.next

        return dummy.next


