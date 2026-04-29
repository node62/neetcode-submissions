class Solution:
    def isHappy(self, n: int, seen=None) -> bool:
        # Initialize seen only on the very first call
        if seen is None:
            seen = set()
            
        if n == 1:
            return True
        elif n in seen:
            return False
            
        seen.add(n)
        
        # Calculate sum of squares
        temp = 0
        while n:
            n, rem = divmod(n, 10)
            temp += rem**2
            
        # Pass the 'seen' set to the next recursive step
        return self.isHappy(temp, seen)