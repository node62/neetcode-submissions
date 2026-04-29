# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        ans = 0
        def helper(root, maxv):
            nonlocal ans 
            if not root: return 
            if root.val >= maxv: 
                ans += 1
                maxv = root.val
            helper(root.left, maxv)
            helper(root.right, maxv)
        helper(root, root.val - 1)
        return ans