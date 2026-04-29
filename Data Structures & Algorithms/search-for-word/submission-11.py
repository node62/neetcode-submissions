class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        R = len(board)
        C = len(board[0])

        def solve(i, j, l):
            if l == len(word): 
                return True
            
            if l == 0 and i == R:
                return False

            path_found = False
            if 0 <= i < R and 0 <= j < C and board[i][j] == word[l]:
                temp = board[i][j]
                board[i][j] = '#'
                
                if (solve(i+1, j, l+1) or 
                    solve(i-1, j, l+1) or 
                    solve(i, j+1, l+1) or 
                    solve(i, j-1, l+1)):
                    path_found = True
                
                board[i][j] = temp

            if path_found:
                return True

            if l == 0:
                next_i, next_j = i, j + 1
                if next_j == C:
                    next_i += 1
                    next_j = 0
                return solve(next_i, next_j, 0)

            return False

        return solve(0, 0, 0)
