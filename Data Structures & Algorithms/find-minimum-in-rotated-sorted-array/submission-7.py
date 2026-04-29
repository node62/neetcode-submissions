# 2nd try
class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        low, high = 0, n-1
        res = float('inf')
        while low<=high:
            mid = (low + high) // 2
            if nums[mid] <= nums[high]:
                high = mid - 1
                res = min(res, nums[mid])
            else:
                low = mid+1

        return res 