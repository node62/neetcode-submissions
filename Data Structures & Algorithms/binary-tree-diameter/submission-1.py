# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        md = 0
        def height(root):
            nonlocal md
            if not root: return 0
            A = height(root.left)
            B = height(root.right)
            md = max(md, A + B + 1)
            return max(A, B) + 1
        height(root)
        return md - 1
