from heapq import *
class MedianFinder:

    def __init__(self):
        self.small = [] # max heap 
        self.large = [] # min heap

    def addNum(self, num: int) -> None:

        # 1st element
        if len(self.small) == len(self.large) == 0:
            heappush_max(self.small, num)
            return 
        
        # 2nd element
        elif len(self.small) == 1 and len(self.large) == 0:
            heappush_max(self.small, num)
            temp = heappop_max(self.small)

            heappush(self.large, temp)
            return
        
        if num <= self.small[0]:
            heappush_max(self.small, num)
        else:
            heappush(self.large, num)
        
        if abs( len(self.small) - len(self.large) ) > 1:
            if len(self.small) < len(self.large):
                temp = heappop(self.large)
                heappush_max(self.small, temp)
            
            elif len(self.small) > len(self.large):
                temp = heappop_max(self.small)
                heappush(self.large, temp)

    def findMedian(self) -> float:
        print('small: ', self.small)
        print('large: ', self.large)
        print()

        if len(self.small) == len(self.large):
            return (self.small[0] + self.large[0]) / 2

        elif len(self.small) < len(self.large):
            return self.large[0]

        elif len(self.small) > len(self.large):
            return self.small[0]