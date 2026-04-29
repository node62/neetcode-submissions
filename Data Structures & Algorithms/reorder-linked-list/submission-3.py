# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head.next or not head.next.next:
            return 
        slow, fast = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        tail1 = slow
        slow = slow.next
        tail1.next = None
        tail2 = slow

        prev = None
        while slow.next:
            prev, slow.next, slow = slow, prev, slow.next
        slow.next = prev
        
        a = head
        b = slow

        while a and b:
            a.next, a = b, a.next
            b.next, b = a, b.next

