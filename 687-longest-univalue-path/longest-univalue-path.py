# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:

        self.ans = 0
        # same as max diameter of tree --> solve for children
        def dfs(root): # whats the max (answer for left,ans for right)
            if root == None:
                return 0 # no edges
            
            # solve for children first
            left_len = dfs(root.left)
            right_len = dfs(root.right)

            # gate keeper
            edges_to_the_left = 0
            edges_to_the_right = 0

            # check to the left
            if root.left and root.left.val == root.val:
                edges_to_the_left = left_len + 1
            
            # check to the right
            if root.right and root.right.val == root.val:
                edges_to_the_right = right_len + 1

            # update global value (answer)
            self.ans = max(self.ans, edges_to_the_left + edges_to_the_right)

            return max(edges_to_the_left, edges_to_the_right)

        dfs(root)

        return self.ans


            
        