class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        area = 0

        l_wall = [0] * n
        l_max = 0
        r_wall = [0] * n
        r_max = 0

        for i in range(n):
            k = n-1 - i

            if height[i] > l_max:
                l_max = height[i]
            if height[k] > r_max:
                r_max = height[k]

            l_wall[i] = l_max
            r_wall[k] = r_max



        for i in range(n):
            v = height[i]
            l = i-1
            r = i+1
            
            if l_wall[i] > v and r_wall[i] > v:
                area+= min(l_wall[i], r_wall[i]) - v
        
        return area
            
        