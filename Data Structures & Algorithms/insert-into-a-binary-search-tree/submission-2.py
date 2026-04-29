# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val, None, None)
        temp = root
        while temp:
            if val < temp.val:
                if not temp.left:
                    temp.left = TreeNode(val, None, None)
                    break
                else:
                    temp = temp.left
            else:
                if not temp.right:
                    temp.right = TreeNode(val, None, None)
                    break
                else:
                    temp = temp.right
        return root