# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev_end = dummy
        slow = curr = head
        itr = 0
        for i in range(999999999999999):
            if itr and itr%k == 0:
                prev = curr
                temp = slow
                while slow != curr:
                    prev, slow.next, slow = slow, prev, slow.next
                prev_end.next = prev
                prev_end = temp
            itr += 1
            if curr == None:
                break
            curr = curr.next
        return dummy.next