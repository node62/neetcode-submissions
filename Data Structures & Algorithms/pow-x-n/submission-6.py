class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n<0:
            n = -n
            x = 1/x
        ans = 1
        for i in range(n//2):
            ans *= x*x
        if n&1: ans*= x
        return ans