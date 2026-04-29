class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i, v in enumerate(nums):
            comp = target - v
            if v not in d:
                d[comp] = i
            else:
                return [d[v], i]