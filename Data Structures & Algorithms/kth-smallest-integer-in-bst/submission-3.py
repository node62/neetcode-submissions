class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count = 0
        res = 0
        def traverse(node):
            nonlocal count, res
            if not node: return 
            traverse(node.left)
            count += 1
            if count == k:
                res = node.val
                return 
            traverse(node.right)
        traverse(root)
        return res