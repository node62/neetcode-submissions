class Solution:
    def carFleet(self, t: int, p: List[int], s: List[int]) -> int:
        n = len(p)
        stuff = sorted(zip(p, s), key=lambda x:x[0])
        for i in range(n):
            tp, ts = stuff[i]
            stuff[i] = (t - tp) / ts
        curr_min = stuff[-1]
        for i in range(n-2, -1, -1):
            if stuff[i] < curr_min:
                stuff[i] = curr_min
            else:
                curr_min = stuff[i]
        stuff = set(stuff)
        return len(stuff)

