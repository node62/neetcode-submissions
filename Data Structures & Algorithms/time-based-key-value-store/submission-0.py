from collections import defaultdict
class TimeMap:
    def __init__(self):
        self.cache = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.cache[key].append((timestamp, value))


    def get(self, key: str, timestamp: int) -> str:
        if not self.cache[key]:
            return ""
        
        else:
            temp = self.cache
            l, h = 0, len(self.cache[key]) - 1
            res = -1
            while l<=h:
                mid = (l+h)//2
                if temp[key][mid][0] > timestamp:
                    h = mid - 1
                else:
                    l = mid + 1
                    res = mid
                
            return temp[key][res][1] if res != -1 else ""


