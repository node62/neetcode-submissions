class MinHeap:
    
    def __init__(self):
        self.heap = [float('-inf')]

    def push(self, val: int) -> None:
        self.heap.append(val)        
        i = len(self.heap) - 1

        while self.heap[i] < self.heap[i//2]:
            self.heap[i], self.heap[i//2] = self.heap[i//2], self.heap[i]
            i //= 2

    def pop(self) -> int:
        if len(self.heap) == 1:
            return -1
        if len(self.heap) == 2:
            return self.heap.pop()
        
        ans = self.heap[1]
        self.heap[1] = self.heap.pop()
        self.percolate_down(1)
        return ans


    def top(self) -> int:
        if len(self.heap) == 1:
            return -1
        return self.heap[1]

    def heapify(self, nums: List[int]) -> None:
        if nums:
            self.heap = nums
            self.heap.append(self.heap[0])
            self.heap[0] = float('-inf')
            
        cur = (len(self.heap) - 1) // 2
        while cur > 0:
            self.percolate_down(cur)
            cur -= 1


    def percolate_down(self, idx):
        while 2*idx < len(self.heap):
            min_idx = idx
            for j in range(2*idx, min(len(self.heap), 2*idx + 2)):
                if self.heap[min_idx] > self.heap[j]:
                    min_idx = j
            if min_idx == idx:
                break
            else:
                self.heap[min_idx], self.heap[idx] = self.heap[idx], self.heap[min_idx]
                idx = min_idx