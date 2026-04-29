class StockSpanner:

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        ans = 1
        for i in range(len(self.stack)-1, -1, -1):
            if self.stack[i]>price: break
            ans += 1
        self.stack.append(price)   
        return ans
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)