from heapq import *
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for p in points:
            a, b = p
            c = a**2 + b**2
            heap.append( (c, [a, b]) )
        heapify(heap) 
        closest = nsmallest(k, heap)
        ans = []
        for _, p in closest:
            ans.append(p)
        return ans