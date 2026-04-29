class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        add = sum(nums)
        n = len(nums)
        actual = n*(n+1)//2
        return actual - add
        