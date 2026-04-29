# practice time
from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        cache = defaultdict(int)
        L = 0
        n = len(s)
        maxf = 0
        ans = 0
        for R in range(n):
            cache[s[R]] += 1
            maxf = max(maxf, cache[s[R]])
            if (R-L+1) - maxf <= k:
                ans = max(ans, R-L+1)
            else:
                cache[s[L]] -= 1
                L += 1

        return ans
