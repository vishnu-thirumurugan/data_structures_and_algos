# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        node_sum = {None:0}

        def dfs(root): # calculate sum for each node
            if not root:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)

            node_sum[root] = left + right + root.val

            return node_sum[root]

        dfs(root)
     
        res = 0

        for _ , summ in node_sum.items(): # update res based on each edge
            res = max(res, summ * (node_sum[root] - summ))

        
        return res % (10**9 + 7)

            

            

        
        