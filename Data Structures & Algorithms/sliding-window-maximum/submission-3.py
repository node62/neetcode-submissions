# O(n) solution using monotonic queue
from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        monq = deque()
        L = 0 
        ans = []
        for R in range(len(nums)):
            while monq and nums[monq[-1]] < nums[R]:
                monq.pop()
            monq.append(R)

            if R - L + 1 < k:
                continue
            
            ans.append(nums[monq[0]])

            if monq[0] == L:
                monq.popleft()
            L+=1
        
        return ans