from collections import defaultdict
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        log = defaultdict(int)
        for v in nums:
            log[v] += 1
        n = len(nums)
        fin = []
        cur = []
        def bt():
            if len(cur) == n:
                fin.append(cur[:])
                return
            for key in log:
                if log[key] > 0:
                    cur.append(key)
                    log[key]-=1
                    bt()
                    cur.pop()
                    log[key]+=1
        bt()
        return fin 