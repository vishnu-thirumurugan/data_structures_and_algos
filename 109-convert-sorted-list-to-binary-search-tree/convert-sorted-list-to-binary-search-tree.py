# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        # convert sorted linked list into height balanced binary tree

        # base case
        if not head: return None
        if not head.next: return TreeNode(head.val)

        slow = fast = head
        prev = None

        # 1. find the middle
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        # detatch the second half from the head
        prev.next = None

        root = TreeNode(slow.val)

        # recurse for the left
        root.left = self.sortedListToBST(head)

        # recurse for the right
        root.right = self.sortedListToBST(slow.next)  # slow being the root

        return root

        