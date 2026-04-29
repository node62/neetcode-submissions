class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def helper(ptr, op, fin):
            if ptr == len(nums):
                fin.append(op)
                return
            top = nums[ptr]
            ptr+=1
            helper(ptr, op+[top], fin)
            helper(ptr, op, fin)
        fin = []
        helper(0, [], fin)
        return fin

