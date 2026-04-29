class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        last_seen = float('inf')
        nums.sort()
        n = len(nums)
        fin = []
        cur = []
        def bt(i):
            nonlocal last_seen
            if i == n:
                fin.append(cur[:])
                return
            if last_seen == nums[i]:
                bt(i+1)
                return
            cur.append(nums[i]) # include current element
            bt(i+1)
            last_seen = cur.pop() # exclude current element
            bt(i+1)
        bt(0)
        return fin