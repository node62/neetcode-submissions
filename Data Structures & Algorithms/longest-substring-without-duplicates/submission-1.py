class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        max_length = 0
        L = 0
        for R in range(len(s)):
            v = s[R]
            while s[R] in seen:
                seen.discard(s[L])
                L+=1
            seen.add(s[R])
            max_length = max(max_length, len(seen))
        
        return max_length