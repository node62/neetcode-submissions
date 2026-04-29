class Solution:
    def climbStairs(self, n: int) -> int:
        def helper(n):
            if n<0:
                return 0
            if n == 0:
                return 1
            if n in cache:
                return cache[n]
            cache[n] = helper(n-1) + helper(n-2)
            return cache[n]
        cache = {}
        return helper(n)