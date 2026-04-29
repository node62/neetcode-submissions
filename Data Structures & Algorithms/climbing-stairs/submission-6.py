# Using bottom-up approach
class Solution:
    def climbStairs(self, n: int) -> int:
        if n<2: return n

        dp = [0]*(n+1)

        old = new = 1

        for i in range(2, n+1):
            old, new = new, new+old
        
        return new