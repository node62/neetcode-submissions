# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def Insert(root, val):
            node = TreeNode(val)
            prev, temp = root, root
            while temp:
                prev = temp
                temp = temp.left if check[val] < check[temp.val] else temp.right
            if check[val] < check[prev.val]:
                prev.left = node
            else:
                prev.right = node
            return root

        check = {}
        root = TreeNode(preorder[0])
        n = len(inorder)

        for i in range(n):
            check[inorder[i]] = i            
        
        for i in range(1, n):
            root = Insert(root, preorder[i])
        
        return root