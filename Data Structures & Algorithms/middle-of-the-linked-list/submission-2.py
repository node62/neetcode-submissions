# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow, fast = head, head
        rate = 2
        while True:
            for i in range(rate):
                if fast:
                    fast = fast.next
                else:
                    return slow
            slow = slow.next