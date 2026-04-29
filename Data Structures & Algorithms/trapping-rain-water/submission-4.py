class Solution:
    def trap(self, h: List[int]) -> int:
        if not h:
            return 0

        n = len(h)
        l, r = 0, n-1
        l_max, r_max = h[l], h[r]

        area = 0

        while l < r:
            if l_max < r_max:
                l+=1
                l_max = max(l_max, h[l])
                area += l_max - h[l]
            else:
                r-=1
                r_max = max(r_max, h[r])
                area += r_max - h[r]
                
        return area