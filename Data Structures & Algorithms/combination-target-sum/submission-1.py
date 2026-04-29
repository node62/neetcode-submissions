class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        fin = []
        cur = []
        def bt(i, sum_cur):
            if sum_cur >= target:
                if sum_cur == target:
                    fin.append(cur[:])
                return
            if i>=len(nums): return
            
            cur.append(nums[i])
            # sum_cur += nums[i]
            bt(i, sum_cur + nums[i])
            L = cur.pop()
            bt(i+1, sum_cur)

        bt(0, 0)
        return fin
        