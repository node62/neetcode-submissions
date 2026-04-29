from functools import cache
class Solution:
    def climbStairs(self, n: int) -> int:
        @cache
        def helper(n):
            if n<0:
                return 0
            if n == 0:
                return 1
            return helper(n-1) + helper(n-2)
        return helper(n)