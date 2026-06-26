from heapq import *
class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:

        p_heap = [] # max profit heap
        c_heap = [[c, p] for c, p in zip(capital, profits)] # min capacity heap

        heapify(c_heap) #T:O(n)

        i = 0
        while i < k:
            tag = False
            while c_heap and w >= c_heap[0][0]:
                heappush_max(p_heap, heappop(c_heap)[1])   
                tag = True
            if not tag and not p_heap: break
            w += heappop_max(p_heap)
            i += 1
        return w
