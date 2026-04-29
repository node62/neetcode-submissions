import bisect
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        n = len(arr)
        R = bisect.bisect_left(arr, x)
        L = R-1
        ans = []
        for i in range(k):
            abL = abs(arr[L] - x) if L > -1 else float('inf')
            abR = abs(arr[R] - x) if R < n else float('inf')
            if (abL < abR) or (abL == abR and arr[L] < arr[R]):
                ans.append(arr[L])
                L-=1
            else:
                ans.append(arr[R])
                R += 1
        ans.sort()
        return ans


        