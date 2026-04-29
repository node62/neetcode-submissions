# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.stack = []
        def inorder(root):
            if not root: return 
            inorder(root.left)
            self.stack.append(root)
            inorder(root.right)
        inorder(root)
        self.idx = -1
        self.size = len(self.stack)

    def next(self) -> int:        
        self.idx += 1
        return self.stack[self.idx].val

    def hasNext(self) -> bool:
        if self.idx == self.size - 1: return False
        return True 

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()