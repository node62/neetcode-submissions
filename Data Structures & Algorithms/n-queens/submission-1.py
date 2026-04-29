from collections import defaultdict
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def y_int(i, j, slope):
            return j - slope*i

        def make_queens(arr):
            temp = []
            for i in arr:
                dots = ['.'] * len(arr) 
                dots[i] = 'Q'
                temp.append("".join(dots))
            return temp

        def backtrack(i):
            if i == n:
                temp = make_queens(cur)
                fin.append(temp)
                return 
            
            for j in range(n):
                up_d = y_int(i, j, 1)
                down_d = y_int(i, j, -1)
                if not (
                    j in log['cols']or \
                    up_d in log['up'] or \
                    down_d in log['down']):
                    cur.append(j)

                    log['cols'].add(j)
                    log['down'].add(down_d)
                    log['up'].add(up_d)

                    backtrack(i+1)
                    cur.pop()

                    log['cols'].discard(j)
                    log['down'].discard(down_d)
                    log['up'].discard(up_d)
        
        fin = []
        cur = []
        
        log = defaultdict(set)
        backtrack(0)
        return fin