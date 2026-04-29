class Solution:
    def reverse(self, x: int) -> int:
        MIN = -(2**31)
        MAX = (2**31) - 1 
        ans = int(str(abs(x))[::-1]) 
        if x<0: ans = -ans
        if not MIN <= ans <= MAX:
            return 0
        return ans
        