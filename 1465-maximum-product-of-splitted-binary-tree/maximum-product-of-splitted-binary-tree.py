# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        node_sum = {None:0}

        def dfs(root):
            if not root:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)

            node_sum[root] = left + right + root.val

            return node_sum[root]

        dfs(root)
        self.res = 0
        def dfs(node):
            if not node:
                return 
            self.res = max(self.res, node_sum[node]*(node_sum[root]-node_sum[node]))

            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return self.res % (10**9 + 7)

            

            

        
        