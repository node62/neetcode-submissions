class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def y_int(i, j, slope):
            return j - slope*i
        cols = set()
        up_dia = set()
        down_dia = set()

        def make_queens(arr):
            temp = []
            for i in arr:
                dots = ['.'] * len(arr) 
                dots[i] = 'Q'
                temp.append("".join(dots))
            return temp

        fin = []
        cur = []
        def backtrack(i):
            if i == n:
                temp = make_queens(cur)
                fin.append(temp)
                return 
            
            for j in range(n):
                up_d = y_int(i, j, 1)
                down_d = y_int(i, j, -1)
                if not (
                    j in cols or \
                    up_d in up_dia or \
                    down_d in down_dia):
                    cur.append(j)

                    cols.add(j)
                    down_dia.add(down_d)
                    up_dia.add(up_d)

                    backtrack(i+1)
                    cur.pop()

                    cols.discard(j)
                    down_dia.discard(down_d)
                    up_dia.discard(up_d)
        
        backtrack(0)
        return fin

        