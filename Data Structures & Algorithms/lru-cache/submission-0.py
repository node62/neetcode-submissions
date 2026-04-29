class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.size = 0
        self.d = {}
        

    def get(self, key: int) -> int:
        if key in self.d:
            x = self.d[key]
            del self.d[key]
            self.d[key] = x
            return x
        return -1        

    def put(self, key: int, value: int) -> None:
        if key in self.d:
            del self.d[key]
            self.d[key] = value

        elif self.size < self.cap:
                self.d[key] = value
                self.size+=1

        else:
            del self.d[next(iter(self.d))]
            self.d[key] = value

                
