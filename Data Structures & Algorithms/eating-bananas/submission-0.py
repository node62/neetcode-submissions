from math import ceil
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low, high = 1, max(piles)
        def check(k):
            total = 0
            for i in range(len(piles)):
                total += ceil(piles[i]/k)
            if total > h:
                return 1
            elif total <= h:
                return -1

        while low <= high:
            mid = (low + high) // 2
            if check(mid) > 0:
                low = mid + 1
            elif check(mid) < 0:
                high = mid - 1
        return low
        