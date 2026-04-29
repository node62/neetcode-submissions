class Solution:
    def dailyTemperatures(self, t: List[int]) -> List[int]:
        n = len(t)
        stack = []
        ans = [0] * n
        for i in range(n):
            v = t[i]
            while stack and t[stack[-1]] < v:
                top_idx = stack.pop()
                ans[top_idx] = i - top_idx
            stack.append(i)
        return ans