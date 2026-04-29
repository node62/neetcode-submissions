class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0 
        right = len(s) - 1
        valid = "qwertyuiopasdfghjklzxcvbnm1234567890"

        while left < right:
            if s[left].lower() not in valid:
                left+=1
                continue

            if s[right].lower() not in valid:
                right-=1
                continue
            
            if s[right].lower() != s[left].lower():
                return False
            
            print(s[left], s[right]) 
            left += 1
            right -= 1
        
        return True
            
            