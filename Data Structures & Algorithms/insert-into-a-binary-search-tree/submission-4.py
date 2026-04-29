class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)
        
        curr, parent = root, None
        
        while curr:
            parent = curr
            curr = curr.left if val < curr.val else curr.right
            
        if val < parent.val:
            parent.left = TreeNode(val)
        else:
            parent.right = TreeNode(val)
            
        return root