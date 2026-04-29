class Solution:
    def myPow(self, x: float, n: int) -> float:
        # Handle the negative exponent case
        if n < 0:
            x = 1 / x
            n = -n
        
        ans = 1
        curr = x
        k = 3
        while n > 0:
            # If n is odd, multiply the result by the current power of x
            rem = n % k
            for i in range(rem):
                ans *= curr
            
            # Square the base and halve the exponent
            temp = 1
            for i in range(k):
                temp *= curr
            curr = temp
            n //= k

        return ans