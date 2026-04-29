class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minv = float('inf')
        res = float('-inf')
        for v in prices:
            if v < minv:
                minv = v
            res = max(v-minv, res)
        return res