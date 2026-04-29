# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head or not head.next:
            return None
        tail = head
        arr = []
        while tail:
            arr.append(tail)
            tail = tail.next
        total = len(arr)
        rem = arr[total - n]
        if rem == head:
            head = head.next
            return head
        prev = arr[total - n - 1]
        prev.next = rem.next 
        return head