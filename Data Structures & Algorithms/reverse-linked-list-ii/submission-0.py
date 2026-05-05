# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        def reverse(head, size):
            tail = head
            prev = None
            for _ in range(size):
                tail.next, tail, prev = prev, tail.next, tail
            return prev, head, tail

        dummy = ListNode(0, head)
        tail = head
        prev = dummy 
        size = right - left + 1
        if size == 1: return head
        cnt = 1
        while True:
            if cnt == left:
                ph, pt, x = reverse(tail, size)
                prev.next = ph
                pt.next = x
                break
            prev = prev.next
            cnt += 1
            tail = tail.next

        return dummy.next