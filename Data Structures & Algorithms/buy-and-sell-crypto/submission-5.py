# single pass to find the min till now
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        minv = float('inf')
        res = float('-inf')
        for v in prices:
            if v < minv:
                minv = v
            res = max(v-minv, res)
        return res 