# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.res = -math.inf # bridge --> path sum
        def  helper(root): # returns max of left and right path sum
            if root is None:
                return 0

            left_sum = helper(root.left)
            right_sum = helper(root.right)

            curr_sum = root.val + max(left_sum,0) + max(right_sum,0) # handling negative numbers

            self.res = max(self.res, curr_sum)

            return root.val + max(left_sum, right_sum, 0) # leg

        helper(root)
        return self.res




        