from heapq import *
from collections import deque

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        dex = Counter(tasks)
        heap = [[val, key] for key, val in dex.items()]
        heapify_max(heap)

        que = deque()
        valid = 0

        cycle = 0
        while heap or valid:
            if len(que) == n+1:
                free = que.popleft()
                if free:
                    valid -= 1
                    heappush_max(heap, free)
        
            if heap:
                done = heappop_max(heap)
                done[0] -= 1

                if done[0]:
                    # print(done[1])
                    que.append(done)
                    valid += 1
                else:
                    que.append(None)
                    # print(None)
                    
            else:
                que.append(None)
                # print(None)


            cycle += 1
        return cycle 