# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:
    # do simple inorder traversal for this

    def __init__(self, root: Optional[TreeNode]):
        self.inorderStack = []

        def inorderTraversal(node):
            if not node:
                return
            
            inorderTraversal(node.left)
            self.inorderStack.append(node.val)
            inorderTraversal(node.right)

        inorderTraversal(root)   # now the stack is full
        self.index = 0
        self.n = len(self.inorderStack)

    def next(self) -> int:
        val = self.inorderStack[self.index]
        self.index += 1 # move the pointer
        return val

    def hasNext(self) -> bool:
        return self.index < self.n


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()