class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root: return None
        curr = root
        if q.val > curr.val and p.val > curr.val:
            curr = self.lowestCommonAncestor(curr.right, p, q)
        elif q.val < curr.val and p.val < curr.val:
            curr = self.lowestCommonAncestor(curr.left, p, q)
        return curr