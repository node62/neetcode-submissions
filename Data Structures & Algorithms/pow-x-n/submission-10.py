class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n<0: x = 1/x
        def helper(x, n):
            if n==0: return 1
            res = helper(x*x, n//2)
            return x * res if n%2 else res
        
        return helper(x, abs(n))