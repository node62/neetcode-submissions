class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        fin = []
        n = len(nums)
        def helper(i):
            if i == n:
                fin.append(nums[:])
                return 
            for j in range(i, n):
                nums[i], nums[j] = nums[j], nums[i]
                helper(i+1)
                nums[i], nums[j] = nums[j], nums[i]
        helper(0)
        return fin