# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        tail = head
        n = 0
        while tail:
            tail = tail.next 
            n+=1
        dummy = ListNode(0, head)
        too_slow = dummy
        slow = curr = head
        itr = 0
        while itr <= n:
            if itr and itr%k == 0:
                prev = curr
                start = slow
                while slow != curr:
                    prev, slow.next, slow = slow, prev, slow.next
                too_slow.next = prev
                too_slow = start
            curr = curr and curr.next
            itr += 1
        return dummy.next