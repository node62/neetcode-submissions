# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr = l1
        num1 = 0
        mul = 1
        while curr:
            num1 = mul * curr.val + num1
            curr = curr.next
            mul *= 10
        curr = l2
        num2 = 0
        mul = 1
        while curr:
            num2 = curr.val * mul + num2
            curr = curr.next
            mul *= 10
        sumv = num1 + num2
        rem = sumv % 10
        sumv = sumv//10
        fin = ListNode(rem, None)
        curr = fin
        while sumv:
            rem = sumv % 10
            sumv = sumv//10
            curr.next = ListNode(rem, None) 
            curr = curr.next
        return fin