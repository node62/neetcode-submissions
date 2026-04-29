class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n<0: x = 1/x
        def helper(x, n):
            if n==0: return 1
            print(x)
            if n%2:
                return helper(x*x, n//2) * x
            else:
                return helper(x*x, n//2)
        return helper(x, abs(n))