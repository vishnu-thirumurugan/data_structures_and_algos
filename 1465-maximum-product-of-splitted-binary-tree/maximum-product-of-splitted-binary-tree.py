# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:

        subtree_sum = {}

        def traversal1(root):
            # calculates sum of subtree nodes
            if root == None:
                return 0

            left = traversal1(root.left)
            right = traversal1(root.right)

            subtree_sum[root] =  left + right + root.val

            return subtree_sum[root]
        traversal1(root)

        total = subtree_sum[root]
        ans = 0
        for node, val in subtree_sum.items():
            ans = max(ans, (total-val)*val)

        return (ans)%(10**9+7)

            

        

            

            

        
        