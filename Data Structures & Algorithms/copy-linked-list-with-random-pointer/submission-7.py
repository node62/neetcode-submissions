"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        on = {None:None}
        tail =  head
        while tail:
            on[tail] = Node(tail.val, None, None)
            tail = tail.next
        tail = head
        while tail:
            on[tail].next = on[tail.next] 
            on[tail].random = on[tail.random] 
            tail = tail.next
        return on[head] 