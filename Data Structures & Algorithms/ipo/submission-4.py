from heapq import *
class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:

        p_heap = [] # max profit heap
        c_arr = sorted(zip(capital, profits), reverse=True)

        i = 0
        while i < k:
            n0 = len(p_heap)
            while c_arr and w >= c_arr[-1][0]:
                heappush_max(p_heap, c_arr.pop()[1])   
            n1 = len(p_heap)
            if n1 == n0 == 0: break
            w += heappop_max(p_heap)
            i += 1
        return w
