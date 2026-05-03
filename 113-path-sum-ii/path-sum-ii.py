# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], target: int) -> List[List[int]]:
        res = []

        def dfs(curr, path, curr_sum):
            if not curr:
                return 
            
            # update the node value
            path.append(curr.val)
            curr_sum += curr.val

            if not curr.left and not curr.right and curr_sum == target:
                res.append(path[:])

            else: # explore till last
                dfs(curr.left, path, curr_sum)
                dfs(curr.right, path, curr_sum)
            
            path.pop()

        dfs(root, [], 0)
        return res


            
        