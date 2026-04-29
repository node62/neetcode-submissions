class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        nums = range(1, n+1)
        fin = [] 
        cur = []
        def dfs(i):
            nonlocal k
            if len(cur) == k:
                fin.append(cur[:])
                return
            if i == len(nums):
                return 
            cur.append(nums[i])
            dfs(i+1)
            cur.pop()
            dfs(i+1)
        dfs(0)
        return fin
        