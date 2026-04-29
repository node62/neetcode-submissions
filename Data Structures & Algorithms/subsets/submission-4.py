import copy
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        temp = []
        def backtrack(itr):
            if  itr >= len(nums):
                res.append(copy.copy(temp))
                return 
            backtrack(itr+1)
            temp.append(nums[itr])
            backtrack(itr+1)
            temp.pop()
        
        backtrack(0)
        return res