class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n<0: x = 1/x
        def helper(x, n):
            if n==0: return 1
            res = helper(x*x*x*x, n//4)
            match n%4:
                case 1:
                    res *= x
                case 2:
                    res *= x*x
                case 3:
                    res *= x*x*x
            return res
        
        return helper(x, abs(n))