class Solution:
    def carFleet(self, t: int, p: List[int], s: List[int]) -> int:
        n = len(p)
        time = []

        for tp, ts in zip(p, s):
            time.append((t-tp)/ts)

        indices = range(n)
        indices = sorted(indices, key=lambda i: p[i])
        time = [time[i] for i in indices]

        curr_min = time[-1]
        for i in range(n-2, -1, -1):
            if time[i] < curr_min:
                time[i] = curr_min
            else:
                curr_min = time[i]
        time = set(time)
        return len(time)

