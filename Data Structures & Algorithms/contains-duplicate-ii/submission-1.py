class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if not k:
            return False
            
        q = deque()

        for v in nums:
            if v in q:
                return True

            if len(q) < k:
                q.append(v)
            else:
                q.popleft()
                q.append(v)
            
        
        return False