class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        for i in range(k):
            minv = min(nums)
            idx = nums.index(minv)
            nums[idx] *= multiplier
        return nums
        