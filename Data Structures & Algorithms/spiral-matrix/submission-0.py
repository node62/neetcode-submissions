class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ans = []        
        m = len(matrix)
        n = len(matrix[0])
        x, y = 0, 0
        dir = 'E'

        def move(x, y, dir):
            match dir:
                case 'N':
                    return x-1, y
                case 'E':
                    return x, y+1
                case 'S':
                    return x+1, y
                case 'W':
                    return x, y-1

        def change_dir(dir):
            arr = ['N', 'E', 'S', 'W']
            return arr[(arr.index(dir) + 1) % 4]

        for i in range(m*n):
            ans.append(matrix[x][y])
            matrix[x][y] = '*'
            tx, ty = move(x, y, dir)
            itr = 0
            if i != m*n -1:
                while not (0<= tx < m and 0<= ty < n) or matrix[tx][ty] == '*':
                    dir = change_dir(dir)
                    tx, ty = move(x, y, dir)
            
            x, y = tx, ty
        
        return ans
        
