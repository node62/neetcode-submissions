# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, None)
        carry = 0 
        curr = dummy 
        while l1 or l2:
            A = l1 and l1.val or 0
            B = l2 and l2.val or 0

            sumv = A + B + carry 
            add = sumv % 10
            carry = sumv // 10
            nnode = ListNode(add, None)
            curr.next = nnode
            curr = curr.next

            l1 = l1 and l1.next
            l2 = l2 and l2.next
        if carry:
            curr.next = ListNode(carry, None)

        return dummy.next
