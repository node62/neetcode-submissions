class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n<0: x = 1/x
        def helper(x, n):
            if n==0: return 1
            print(x)
            if n%2:
                res = helper(x*x, n//2) * x
            else:
                res = helper(x*x, n//2)
            return res
        return helper(x, abs(n))