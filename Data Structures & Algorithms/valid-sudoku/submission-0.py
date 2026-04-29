class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = len(board)

        rmap = [set() for _ in range(n)]
        cmap = [set() for _ in range(n)]
        gmap = [set() for _ in range(n)]


        for i in range(n):
            for j in range(n):
                val = board[i][j]
                if val == '.':
                    continue
                k = 3 * (i//3) + (j//3)
                if (val in rmap[i]) or (val in cmap[j]) or (val in gmap[k]):
                    return False
                rmap[i].add(val)
                cmap[j].add(val)
                gmap[k].add(val)
        
        return True