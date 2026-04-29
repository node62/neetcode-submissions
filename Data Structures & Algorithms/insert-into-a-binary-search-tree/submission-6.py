# Iterative method (Can be better)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)
        prev, curr = None, root
        while curr:
            prev = curr
            curr = curr.left if val < curr.val else curr.right 
        nnode = TreeNode(val)
        if val < prev.val:
            prev.left = nnode
        else:
            prev.right = nnode
        return root