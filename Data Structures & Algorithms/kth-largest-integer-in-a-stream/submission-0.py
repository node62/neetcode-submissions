class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = [float('-inf')] 
        for i in range(len(nums)):
            v = nums[i]
            self.add(v)

    def add(self, val: int) -> int:
        self.push(val)
        if len(self.heap) > self.k + 1:
            self.pop()
        return self.heap[1]

    def push(self, val:int) -> None:
        self.heap.append(val)
        i = len(self.heap) - 1
        while self.heap[i] < self.heap[i//2]:
            self.heap[i], self.heap[i//2] = self.heap[i//2], self.heap[i]
            i //= 2

    def pop(self):
        if len(self.heap) == 1:
            return None
        if len(self.heap) == 2:
            return self.heap.pop()
        last = self.heap.pop()
        i = 1
        self.heap[i] = last 
        while 2*i < len(self.heap):
            min_idx = i
            for j in range(2*i, min(len(self.heap), 2*(i+1))):
                if self.heap[min_idx] > self.heap[j]:
                    min_idx = j
            if min_idx == i :
                break
            else:
                self.heap[min_idx], self.heap[i]  = self.heap[i], self.heap[min_idx]
                i = min_idx
        