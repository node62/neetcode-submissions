# using binary search
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = len(nums1)
        n = len(nums2)

        is_odd = ((m+n)%2 == 1)

        if m > n:
            nums1, nums2 = nums2, nums1
            m, n = n, m
        
        half = (m+n)//2


        l, r = 0, m
        while l<=r:
            mid = (l+r) // 2
        
            m1 = nums1[mid - 1] if mid != 0 else float('-inf')
            m2 = nums1[mid] if mid != m else float('inf')

            i1 = nums2[half - mid - 1] if half - mid - 1 >= 0 else float('-inf')
            i2 = nums2[half - mid] if half - mid < n else float('inf')

            if max(m1, i1) <= min(m2, i2):
                A= max(m1, i1)
                B= min(m2, i2)
                break
            
            elif m1 > i2:
                r = mid - 1
            
            elif i1 > m2:
                l = mid + 1

        return B if is_odd else (A+B)/2