class Solution:
    def dailyTemperatures(self, t: List[int]) -> List[int]:
        n = len(t)
        stack = [(t[0], 0)]
        ans = [0] * n
        for i in range(1, n):
            v = t[i]
            while stack and stack[-1][0] < v:
                tv, ti = stack.pop()
                ans[ti] = i - ti
            stack.append((v, i))

        return ans 
