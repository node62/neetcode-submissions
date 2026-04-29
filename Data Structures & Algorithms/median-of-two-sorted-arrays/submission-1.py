import statistics as st
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A = B = 0
        m = len(nums1)
        n = len(nums2)

        is_odd = (m+n)%2

        arr = []

        for i in range((m+n)//2+1):
            if A < m and B < n:
                if nums1[A] < nums2[B]:
                    arr.append(nums1[A])
                    A+=1
                else:
                    arr.append(nums2[B])
                    B+=1

            elif A < m:
                arr.append(nums1[A])
                A+=1
                
            elif B < n:
                arr.append(nums2[B])
                B+=1
        
        if is_odd:
            return arr[-1]
        
        else:
            return (arr[-1] + arr[-2]) / 2