class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False

        m = len(matrix)
        n = len(matrix[0])

        low, high = 0, m*n-1

        while low <= high:
            mid = (low+high)//2
            mr = mid // n
            mc = mid % n

            if target < matrix[mr][mc]:
                high = mid -1
            elif target > matrix[mr][mc]:
                low = mid +1
            else:
                return True
        
        return False