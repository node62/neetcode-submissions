class Solution:
    def mySqrt(self, x: int) -> int:
        ans = -1
        low, high = 0, x
        while low <= high:
            mid = (low + high) // 2
            if mid ** 2 > x:
                high = mid - 1
            else:
                low = mid + 1 
                ans = mid
        return ans;