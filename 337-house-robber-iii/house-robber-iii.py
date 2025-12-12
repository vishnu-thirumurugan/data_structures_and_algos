# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# recursion solution
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        @lru_cache(None)
        def helper(root):
            if root == None:
                return 0

            # take current node
            rob_current =root.val
            if root.left:
                rob_current += helper(root.left.left) + helper(root.left.right)
            if root.right:
                rob_current += helper(root.right.left) + helper(root.right.right)

            # leave rhe current node
            not_rob_current = helper(root.left) + helper(root.right)

            return max(rob_current, not_rob_current)

        return helper(root)

        

        