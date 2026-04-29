# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# this variation of the solution lets you set a rate for the fast pointer
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow, fast = head, head
        rate = 2
        while True:
            for i in range(rate):
                if fast == None:
                    return slow
                else:
                    fast = fast.next
            slow = slow.next