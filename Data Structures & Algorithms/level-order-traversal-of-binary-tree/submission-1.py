class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        try:
            if not root: return []
            fin = []
            q = deque([root])
            
            while q:
                temp = []
                for i in range(len(q)):
                    curr = q.popleft()
                    print(f"DEBUG: curr is {curr}, i is {i}", flush=True)            
                    if curr.left: q.append(curr.left)
                    if curr.right: q.append(curr.right)
                    temp.append(curr.val)
                fin.append(temp)
            return fin

        except Exception as e:
            print(f"CRASHED WITH ERROR: {e}", flush=True)
            if 'curr' in locals():
                print(f"LAST CURR VALUE: {curr}", flush=True)
            raise e