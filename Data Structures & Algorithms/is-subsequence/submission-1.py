class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s: return True
        sp = 0
        for c in t:
            if c == s[sp]:
                sp+=1
            if sp == len(s):
                return True
        return False