# using linked lists
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class MyCircularQueue:

    def __init__(self, k: int):
        self.k = k 
        self.size = 0
        self.head = None        
        self.tail = None

    def enQueue(self, value: int) -> bool:
        if not self.isFull():
            if self.isEmpty():
                self.head = Node(value)
                self.tail = self.head
            else:
                temp = Node(value)        
                self.tail.next = temp
                self.tail = self.tail.next
            # self.tail.next = self.head
            self.size += 1
            return True
        else:
            return False

    def deQueue(self) -> bool:
        if not self.isEmpty():
            self.head = self.head.next
            # self.tail.next = self.head
            self.size -= 1
            return True
        else:
            return False
        

    def Front(self) -> int:
        if not self.isEmpty():
            return self.head.val
        else:
            return -1
        

    def Rear(self) -> int:
        if not self.isEmpty():
            return self.tail.val
        else:
            return -1
        

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.k
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()