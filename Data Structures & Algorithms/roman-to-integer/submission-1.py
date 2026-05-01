class Solution:
    def romanToInt(self, s: str) -> int:
        table = {
            'I':             1,
            'V':             5,
            'X':             10,
            'L':             50, 
            'C':             100, 
            'D':             500, 
            'M':             1000
        }
        
        n = len(s)
        curr = 0
        ans = 0
        for i in range(n-1, -1, -1):
            val = table[s[i]]
            if curr <= val:
                curr = val
            else:
                val = -val
            ans += val
        
        return ans
