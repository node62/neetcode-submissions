import math
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        pad = 0
        n = len(matrix)
        r = math.floor(n/2)
        for i in range(r):
            for j in range(pad, n-pad-1):
                # print(i, j, end=': ')
                # print(matrix[i][j])
                # print(matrix[i][~j])
                # print(matrix[~i][j])
                # print(matrix[~i][~j])
                matrix[i][j], matrix[j][~i], matrix[~i][~j], matrix[~j][i] = \
                matrix[~j][i], matrix[i][j], matrix[j][~i], matrix[~i][~j]
            print()
            pad += 1
            