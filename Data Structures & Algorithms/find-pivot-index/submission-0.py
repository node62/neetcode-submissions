class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        p = [0] * (n+1)
        total = sum(nums)
        for i in range(n):
            p[i+1] = nums[i] + p[i]
            if p[i] == total - p[i+1]:
                return i
                        
        return -1
