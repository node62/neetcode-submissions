class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        ans = []
        for v in nums:
            q.append(v)
            if len(q) < k:
                continue
            ans.append(max(q))
            q.popleft() 
        
        return ans