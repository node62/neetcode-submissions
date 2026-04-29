class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        nums = range(1, n+1)
        fin = []
        cur = []
        def dfs(i):
            if len(cur) == k:
                fin.append(cur[:])
                return 
            if i >= n: return 
            
            for j in range(i, n):
                cur.append(nums[j])
                dfs(j+1)
                cur.pop()
        dfs(0)
        return fin