class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        count = 0
        def traverse(node):
            nonlocal count
            if not node:
                return None
            
            # 1. Search Left
            left_res = traverse(node.left)
            if left_res is not None:
                return left_res
            
            # 2. Process Current Node
            count += 1
            if count == k:
                return node.val
            
            # 3. Search Right
            return traverse(node.right)
            
        return traverse(root)