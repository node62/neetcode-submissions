# practice time
from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        L = 0
        cache = defaultdict(int)
        n = len(s)
        maxf = 0
        ans = 0
        for R in range(n):
            cache[s[R]] += 1
            maxf = max(maxf, cache[s[R]])
            if (R-L+1) <= k + maxf:
                ans = max(ans, R-L+1)
            else:
                cache[s[L]] -= 1
                L += 1
        return ans
