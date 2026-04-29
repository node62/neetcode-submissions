class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        n = len(nums)
        s = set(nums)
        ans = -(1<<32)
        check = set()
        for v in nums:
            if v-1 not in s:
                check.add(v)
        
        for v in check:
            l =1
            while v+1 in s:
                v+=1
                l+=1
            ans = max(ans, l)
        return ans
