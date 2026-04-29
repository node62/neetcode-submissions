class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        fin = []
        temp = []
        def backtrack(i, csum):
            nonlocal target
            if i >= len(nums):
                return
            if csum > target:
                return 
            if csum == target:
                fin.append(temp[:])
                return
            a = nums[i]
            temp.append(a)
            backtrack(i, csum+a)
            temp.pop()
            backtrack(i+1, csum)
        backtrack(0, 0)
        return fin 