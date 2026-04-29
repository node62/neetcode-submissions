# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode(0, None)        
        curr = dummy
        k = len(lists)
        while any(lists):
            min_idx = -1 
            min_val = float('inf')
            for i in range(len(lists)):
                if lists[i] and min_val > lists[i].val:
                    min_val = lists[i].val
                    min_idx = i
            if min_idx == -1: break
            curr.next = lists[min_idx] 
            curr = curr.next
            lists[min_idx] = lists[min_idx].next
        return dummy.next
