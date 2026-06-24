import heapq as h
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        arr = []
        for v in stones:
            h.heappush(arr, -v)

        while len(arr) > 1:
            a = -h.heappop(arr)
            b = -h.heappop(arr)
            if b < a:
                h.heappush(arr, -(a-b))

        return -arr[0] if arr else 0