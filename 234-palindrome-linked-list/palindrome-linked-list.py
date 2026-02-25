# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # middle of linked list 
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # reverse linked list (second half)
        prev = None
        while slow:
            nxt = slow.next
            slow.next = prev
            prev = slow
            slow = nxt
        # print(prev)
        # compare 
        left = head
        right = prev
        while right:
            if left.val != right.val:
                return False
            right = right.next
            left = left.next
            
        return True
            