# two pointers
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        maxP = 0
        for r in range(1, len(prices)):
            profit = prices[r] - prices[l]
            if profit > 0:
                maxP = max(maxP, profit)
            else:
                l=r
            r+=1
        return maxP