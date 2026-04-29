class Solution:
    def scoreOfString(self, s: str) -> int:
        def akshay(i):
            return i if i >= 0 else -i

        ans = 0
        for i in range(1, len(s)):
            ans += (akshay(ord(s[i]) - ord(s[i-1])))
        return ans