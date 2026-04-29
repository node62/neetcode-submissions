class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        zero = nums.count(0)
        if zero > 1:
            return [0] * n
        
        total = 1
        for i in range(n):
            if nums[i] == 0:
                continue
            total *= nums[i]
        
        for i in range(n):
            if zero:
                if nums[i]:
                    nums[i] = 0
                else:
                    nums[i] = total
            else:
                nums[i] = total // nums[i]
        
        return nums