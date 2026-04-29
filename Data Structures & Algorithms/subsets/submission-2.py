class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        temp = []
        def backtrack(itr):
            if  itr >= len(nums):
                res.append(temp[:])
                return 
            temp.append(nums[itr])
            backtrack(itr+1)
            temp.pop()
            backtrack(itr+1)
        
        backtrack(0)
        return res