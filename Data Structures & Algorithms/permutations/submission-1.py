class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        fin = []
        cur = []
        picked = [False] * n
        def bt():
            if len(cur)==n:
                fin.append(cur[:])
                return
            for i in range(n):
                if not picked[i]:
                    cur.append(nums[i])
                    picked[i] = True
                    bt()
                    cur.pop()
                    picked[i] = False
        bt()
        return fin

