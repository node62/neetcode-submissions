class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        to_rem = defaultdict(set)
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    to_rem['r'].add(i)
                    to_rem['c'].add(j)
                   

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i in to_rem['r'] or j in to_rem['c']:
                    matrix[i][j] = 0