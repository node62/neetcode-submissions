# Tree serialisation

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def serialise(root):
            if not root:
                return './'
            return (str(root.val) + '/' + serialise(root.left) + serialise(root.right))
        
        the_tree = serialise(root)
        sub_tree = serialise(subRoot)
        
        print(sub_tree)
        print(the_tree)

        return sub_tree in the_tree