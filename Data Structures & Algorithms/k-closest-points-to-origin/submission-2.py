import heapq as h
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        book = defaultdict(list)
        heap = []
        for s in points:
            a, b = s
            c = a**2 + b**2
            book[c].append(s)
            heap.append(c)

        h.heapify(heap)
        closest = h.nsmallest(k, heap)
        ans = []
        for v in closest:
            ans.append(book[v].pop())
        return ans