# last_removed method
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        visited = [False] * n
        fin = []
        cur = []
        def bt():
            if len(cur) == n:
                fin.append(cur[:])
                return 
            last_removed = float('inf')
            for i in range(n):
                if not visited[i] and nums[i]!=last_removed:
                    visited[i] = True
                    cur.append(nums[i])
                    bt()
                    cur.pop()
                    visited[i] = False
                    last_removed = nums[i]
        bt()
        return fin