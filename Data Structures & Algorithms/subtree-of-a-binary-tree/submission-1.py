# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def same_same(r1, r2):
            if not r1 and not r2: return True
            if not r1 or not r2: return False
            return r1.val == r2.val and same_same(r1.left, r2.left) and \
            same_same(r1.right, r2.right) 
        stack = []
        curr = root
        while curr or stack:
            if curr:
                if curr.val == subRoot.val:
                    check =  same_same(curr, subRoot)
                    if check: return check
                stack.append(curr.right)
                curr = curr.left 
            else:
                curr = stack.pop()
        return False