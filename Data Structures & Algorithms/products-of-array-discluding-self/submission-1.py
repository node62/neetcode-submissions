class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        p = [1] * (n+1)
        rp = [1] * (n+1)

        for i in range(n):
            p[i+1] = p[i]*nums[i]
            rp[-(i+2)] = rp[-(i+1)]*nums[-(i+1)]
        
        for i in range(n):
            nums[i] = p[i] * rp[i+1]
        
        return nums