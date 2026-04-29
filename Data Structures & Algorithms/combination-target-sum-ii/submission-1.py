class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        fin = []
        cur = []

        def bt(i):
            if sum(cur) >= target:
                if sum(cur) == target:
                    fin.append(cur[:])
                return
            last = float('inf')
            for j in range(i, n):
                if nums[j] != last:
                    cur.append(nums[j])
                    bt(j+1)
                    last = cur.pop()
        bt(0)
        return fin
