# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head or not head.next:
            return None
        count = 0
        lead = head
        follow = None
        while lead:
            lead = lead.next
            if count == n:
                follow = head
            elif count > n:
                follow = follow.next
            count += 1
        if not follow:
            head = head.next
        else:
            follow.next = follow.next.next
        return head