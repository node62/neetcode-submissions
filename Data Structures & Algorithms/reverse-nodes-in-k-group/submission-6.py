# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        tail = head
        dummy = ListNode(0, head)
        too_slow = dummy
        slow = curr = head
        itr = 0
        while True:
            if itr and itr%k == 0:
                prev = curr
                start = slow
                while slow != curr:
                    prev, slow.next, slow = slow, prev, slow.next
                too_slow.next = prev
                too_slow = start
            itr += 1
            if curr == None:
                break
            curr = curr.next
        return dummy.next