class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        fin = []
        cur = []
        def bt(i):
            if i == n:
                fin.append(cur[:]) 
                return
            cur.append(nums[i])    
            bt(i+1)
            cur.pop()
            bt(i+1)
        bt(0)
        return fin