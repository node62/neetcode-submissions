# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head or not head.next:
            return None
        total  = 0
        tail, temp = None, head
        while temp:
            temp = temp.next 
            tail = temp
            total+=1
        k = total - n
        if not k:
            head = head.next
            return head
        idx = 0
        prev = None
        temp = head
        while idx<k:
            temp, prev = temp.next, temp
            idx+=1
        prev.next = temp.next
        return head