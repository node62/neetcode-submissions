import heapq as h
class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        h.heapify(nums)              
        self.heap = nums
        self.k = k

    def add(self, val: int) -> int:
        h.heappush( self.heap, val)
        return h.nlargest(self.k, self.heap)[-1]
        
