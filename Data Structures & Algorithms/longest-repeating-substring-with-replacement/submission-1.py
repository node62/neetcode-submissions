from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        book = defaultdict(int)
        L = 0
        maxv = 0
        ans = 0 

        for R in range(len(s)):
            book[s[R]]+=1
            maxv = max(maxv, book[s[R]])
            while (R - L + 1) - maxv > k:
                book[s[L]]-=1
                L+=1

            ans = max(ans, R - L + 1)
        
        return ans 