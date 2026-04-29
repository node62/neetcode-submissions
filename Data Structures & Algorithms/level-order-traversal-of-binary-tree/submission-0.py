from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        feed1 = deque([root])
        feed2 = deque()
        fin = [[root.val]]
        temp = []
        while feed1 or feed2:
            if feed1[0].left:
                feed2.append(feed1[0].left)
            if feed1[0].right:
                feed2.append(feed1[0].right)  
            
            temp.append(feed1.popleft().val)
            if not feed1:
                fin.append(temp)
                temp = []
                feed1 = feed2
                feed2 = deque()
            
        return fin[1:]