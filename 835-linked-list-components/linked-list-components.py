# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def numComponents(self, head: Optional[ListNode], nums: List[int]) -> int:
        count = 0 
        s = set(nums)

        dummy = ListNode(-1)
        dummy.next = head
        prev = dummy
        curr = dummy.next

        while curr:
            if curr.val in s and prev.val not in s:
                count += 1
            prev = curr
            curr = curr.next
            

        return count

        
        