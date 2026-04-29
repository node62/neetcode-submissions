class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        fin = []
        cur = []
        # picked = [False] * n
        pset = set()
        def bt():
            if len(cur)==n:
                fin.append(cur[:])
                return
            for i in range(n):
                if nums[i] not in pset:
                    cur.append(nums[i])
                    # picked[i] = True
                    pset.add(nums[i])
                    bt()
                    cur.pop()
                    pset.discard(nums[i])
                    # picked[i] = False
        bt()
        return fin

