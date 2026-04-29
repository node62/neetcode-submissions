# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        fin = []
        fin += self.inorderTraversal(root.left)
        fin += [root.val]
        fin += self.inorderTraversal(root.right)
        return fin