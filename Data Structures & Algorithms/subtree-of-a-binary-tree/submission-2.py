# Tree serialisation

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def serialise(root, arr):
            if not root:
                arr.append(None)
                return 
            arr.append(root.val)
            serialise(root.left, arr)
            serialise(root.right, arr)

        the_tree = []
        sub_tree = []

        serialise(root, the_tree)
        serialise(subRoot, sub_tree)
        
        sub_tree = ','.join(str(i) for i in sub_tree)
        the_tree = ','.join(str(i) for i in the_tree)
        
        print(sub_tree)
        print(the_tree)

        return sub_tree in the_tree