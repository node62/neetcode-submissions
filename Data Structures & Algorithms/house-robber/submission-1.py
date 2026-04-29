from functools import cache
class Solution:
    def rob(self, nums: List[int]) -> int:
        @cache
        def helper(i):
            if i < 0: return 0
            if i == 0: return nums[0]
            return max(helper(i-1), helper(i-2) + nums[i])
        return helper(len(nums)-1)
        