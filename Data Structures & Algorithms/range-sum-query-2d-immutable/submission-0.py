class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        r = len(matrix)
        c = len(matrix[0])
        self.prefix = [[0] * c for i in range(r)]
        self.prefix[0][0] = matrix[0][0]

        for i in range(1, c):
            self.prefix[0][i] = self.prefix[0][i-1] + matrix[0][i]
        
        for i in range(1, r):
            self.prefix[i][0] = self.prefix[i-1][0] + matrix[i][0]

        for i in range(1, r):
            for j in range(1, c):
                self.prefix[i][j] = self.prefix[i-1][j] + self.prefix[i][j-1] \
                + matrix[i][j] - self.prefix[i-1][j-1]

        print(self.prefix)        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:

        A = self.prefix[row2][col1-1] if col1-1 > -1 else 0
        B = self.prefix[row1-1][col2] if row1-1 > -1 else 0
        C = self.prefix[row1-1][col1-1] if row1-1 > -1 and col1-1 > -1 else 0
        temp = self.prefix[row2][col2] - A \
        - B + C
        return temp

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)