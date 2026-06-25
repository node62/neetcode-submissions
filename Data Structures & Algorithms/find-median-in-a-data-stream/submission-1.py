from heapq import *
class MedianFinder:

    def __init__(self):
        self.small, self.large = [], []        
        self.median = -1

    def addNum(self, num: int) -> None:
        if len(self.small) == len(self.large):
            heappush_max(self.small, heappushpop(self.large, num))
            self.median = self.small[0]
        else:
            heappush(self.large, heappushpop_max(self.small, num))
            self.median = (self.small[0] + self.large[0]) / 2


    def findMedian(self) -> float:
        return self.median