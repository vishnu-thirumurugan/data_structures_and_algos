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
        self.ans = 0
        def traversal2(root):
            if root == None:
                return
            if root.left:
                self.ans = max(self.ans, (total-subtree_sum[root.left])*subtree_sum[root.left])
            traversal2(root.left)
            if root.right:
                self.ans = max(self.ans, (total-subtree_sum[root.right])*subtree_sum[root.right])
            traversal2(root.right)



        traversal2(root)
        return (self.ans)%(10**9 + 7)

            

        

            

            

        
        