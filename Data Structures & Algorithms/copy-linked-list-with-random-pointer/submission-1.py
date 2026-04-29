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
        if not head:
            return None
        cache = {}
        tail = head
        fin = Node(tail.val, None, tail.random)
        slow = fin
        tail = tail.next
        cache = {head: fin}
        while tail:
            nnode = Node(tail.val, None, tail.random)
            slow.next = nnode
            cache[tail] = nnode
            slow, tail = slow.next, tail.next

        slow.next = None

        slow = fin
        while slow:
            slow.random = cache[slow.random] if slow.random else None
            slow = slow.next
        return fin
            