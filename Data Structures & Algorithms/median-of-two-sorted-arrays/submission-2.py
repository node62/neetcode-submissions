import statistics as st
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A = B = 0
        m = len(nums1)
        n = len(nums2)

        is_odd = (m+n)%2
        curr = -1
        prev = -1

        for i in range((m+n)//2+1):
            if A < m and B < n:
                if nums1[A] < nums2[B]:
                    prev = curr
                    curr = nums1[A]
                    A+=1
                else:
                    prev = curr
                    curr = nums2[B]
                    B+=1

            elif A < m:
                prev = curr
                curr = nums1[A]
                A+=1
                
            elif B < n:
                prev = curr
                curr = nums2[B]
                B+=1

        print("curr: ", curr, "\nprev: ", prev)
        if is_odd:
            return curr
        
        else:
            return (curr + prev) / 2