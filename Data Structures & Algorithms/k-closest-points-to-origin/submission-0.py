import heapq as h
class Solution:
    def kClosest(self, m: List[List[int]], k: int) -> List[List[int]]:
        book = defaultdict(list)
        points = []
        for s in m:
            a, b = s
            c = a**2 + b**2
            book[c].append(s)
            points.append(c)

        h.heapify(points)
        closest = h.nsmallest(k, points)
        print(points, closest)
        ans = []
        for v in closest:
            ans.append(book[v].pop())
        return ans