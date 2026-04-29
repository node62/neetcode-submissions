# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root: return True
        def height(root):
            if not root: return True, 0
            bA, hA = height(root.left)
            bB, hB = height(root.right)
            height_info = max(hA, hB) + 1 
            balanced_info = abs(hA - hB) <= 1 and bA and bB 
            return balanced_info, height_info 
        br, hr = height(root)
        return br
