# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head:
            return head

        nodes = []
        curr = head
        while curr:
            nodes.append(curr)
            curr = curr.next

        left = left -1
        right = right-1

        while left < right:
            nodes[left].val, nodes[right].val = nodes[right].val, nodes[left].val
            left += 1
            right -= 1

        return head


        