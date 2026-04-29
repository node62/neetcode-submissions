class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        area = 0
        for i in range(n):
            v = height[i]
            l = i-1
            r = i+1
            
            l_wall = r_wall = 0

            while l >=0:
                l_wall = max(l_wall, height[l])
                l-=1

            while r <n:
                r_wall = max(r_wall, height[r])
                r+=1
            
            if l_wall > v and r_wall > v:
                area+= min(l_wall, r_wall) - v
        
        return area
            
        