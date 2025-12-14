# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        # tree dp --(gemini) -- bottom up
        # states has camera --> (1)
        # 1. needs camera (0) - either child is 0 --> we need to cover child
        # 2. has coverage (2) - either child has camera --> i dont want camera
        # 3. both children are covered (2 and 2)- we could wait and put its camera in its parent

        self.cameras = 0 # global var to count num of cameras

        def dfs(root):
            if root == None: # we consider it has coverage for simplicity
                return 2

            left_state = dfs(root.left)
            right_state = dfs(root.right)

            if left_state == 0 or right_state == 0:
                self.cameras += 1
                return 1 # put camera 
            
            elif left_state == 1 or right_state == 1: # has coverage from child --> tell parent, I am safe
                return 2

            # else: # all my children has coverage --> wait --> parent can give you coverage
                # pass
            return 0 

        # handle for root as well
        root_state = dfs(root)
        if root_state == 0:
            self.cameras += 1
        
        return self.cameras