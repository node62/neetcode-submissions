class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0: return 1.0
        if n < 0:
            x = 1 / x
            n = -n
        
        ans = 1.0
        curr = x
        
        while n > 0:
            rem = n % 10
            
            # 1. Handle the remainder efficiently
            # Instead of a loop, we can use a small 'power' helper 
            # or pre-calculate x^1 through x^9
            if rem > 0:
                ans *= self.small_pow(curr, rem)
            
            # 2. Update curr to curr^10 efficiently
            # curr^10 is (curr^5)^2 or ((curr^2)^2 * curr)^2
            curr = self.small_pow(curr, 10)
            
            n //= 10
            
        return ans

    def small_pow(self, base, p):
        # A mini binary exponentiation just for the small k
        res = 1.0
        while p > 0:
            if p % 2 == 1: res *= base
            base *= base
            p //= 2
        return res