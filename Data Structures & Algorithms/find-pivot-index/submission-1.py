class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        curr = 0
        total = sum(nums)
        for i in range(n):
            nxt = nums[i] + curr
            if curr == total - nxt:
                return i
            curr = nxt

        return -1
