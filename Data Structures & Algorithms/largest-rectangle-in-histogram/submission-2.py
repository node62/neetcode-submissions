class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        h = heights + [-1]
        n = len(h)
        p = [0] * n
        stack = []

        for i in range(n):
            v = h[i]
            while stack and v < h[stack[-1]]:
                idx = stack.pop()
                p[i] += p[idx] + 1
                p[idx] += i - idx
                print(p)
            
            stack.append(i)
        
        final = p[:-1]

        for i in range(n-1):
            final[i] = final[i] * h[i]

        return max(final)
