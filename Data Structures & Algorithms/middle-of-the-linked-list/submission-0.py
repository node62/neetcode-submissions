# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        rate = 2 
        
        slow = head
        fast = head
        count = 0

        while fast:
            fast = fast.next
            count += 1
            if count % rate == 0:
                slow = slow.next
                
        return slow