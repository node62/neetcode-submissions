# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        leng = 0
        temp = head

        while temp:
            leng += 1
            temp = temp.next

        if (leng - n) == 0:
            return head.next

        temp = head
        for index in range(leng - 1):
            if (index + 1) == (leng - n):
                temp.next = temp.next.next
                break
            temp = temp.next

        return head