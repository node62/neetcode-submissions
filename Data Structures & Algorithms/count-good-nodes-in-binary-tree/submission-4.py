
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def helper(root, maxv):
            if not root: return 0
            if root.val >= maxv: 
                maxv = root.val
                return 1 + helper(root.left, maxv) + helper(root.right, maxv)
            return  0 + helper(root.left, maxv) + helper(root.right, maxv)
        final = helper(root, root.val)
        return final