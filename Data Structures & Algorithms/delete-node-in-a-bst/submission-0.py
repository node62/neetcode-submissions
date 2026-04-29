# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        dummy = TreeNode(0, root)
        pprev, curr = dummy, root
        while curr and curr.val != key:
            pprev = curr
            if key < curr.val:
                curr = curr.left
            else:
                curr = curr.right
        if not curr:
            return dummy.left
        if curr.right and curr.left:
            temp = curr.right
            prev = curr
            while temp.left:
                prev = temp
                temp = temp.left
            if prev == curr:
                prev.right = temp.right
            else:
                prev.left = temp.right
            if pprev.left == curr:
                pprev.left = temp
            else:
                pprev.right = temp
            temp.left = curr.left
            temp.right = curr.right
            curr.right = curr.left = None
        else:    
            temp = curr.left or curr.right
            if pprev.left == curr:
                pprev.left = temp
            else:
                pprev.right = temp
            
        return dummy.left