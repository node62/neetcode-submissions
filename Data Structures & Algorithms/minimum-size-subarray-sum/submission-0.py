class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        ans = float('inf')
        L = 0
        curr_sum = 0
        for R in range(len(nums)):
            curr_sum += nums[R]
            while curr_sum >= target:
                ans = min(ans, R-L+1)
                curr_sum -= nums[L]                              
                L+=1
        
        return ans if ans!= float('inf') else 0
