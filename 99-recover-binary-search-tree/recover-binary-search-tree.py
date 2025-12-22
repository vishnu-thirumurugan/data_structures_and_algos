# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        # inorder traversal in BST gives sorted list.
        nodes = []
        vals = []

        def inorder(node):
            if not node:
                return

            inorder(node.left)
            nodes.append(node)
            vals.append(node.val)
            inorder(node.right)

        inorder(root)

        sorted_vals = sorted(vals)

        for i in range(len(vals)):
            if vals[i] != sorted_vals[i]:
                nodes[i].val = sorted_vals[i]


        