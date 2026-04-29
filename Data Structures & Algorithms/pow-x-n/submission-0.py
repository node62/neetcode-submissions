class Solution:
    def myPow(self, x: float, n: int) -> float:
        ans = 1
        if n < 0: x = 1/x
        for i in range(abs(n)):
            print(ans)
            ans *= x
        return ans
