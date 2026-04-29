class Solution:
    def maxArea(self, h: List[int]) -> int:
        m = float('-inf')
        l = 0
        r = len(h) - 1

        while l < r:
            area = (r-l) * min(h[r], h[l])
            if h[r] < h[l]:
                r-=1
            else:
                l+=1
            m = max(area, m)
    
        return m