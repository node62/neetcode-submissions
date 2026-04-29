# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def helper(left, right):
            nonlocal idx
            if left >= right: return None
            root_val = preorder[idx]
            idx += 1
            root = TreeNode(root_val)
            mid = seen[root_val]
            root.left = helper(left, mid)            
            root.right = helper(mid+1, right) 
            return root
        seen = {val:i for i, val in enumerate(inorder)}
        idx = 0
        return helper(0, len(preorder))
