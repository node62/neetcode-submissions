class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        R = len(board)
        C = len(board[0])

        def bt(l, i, j, seen=set()):
            if l == len(word): return True
            if not 0<=i<R or not 0<=j<C: return False
            if word[l] == board[i][j] and \
            (i, j) not in seen:
                seen.add((i, j))
                if bt(l+1, i-1, j, seen): return True
                if bt(l+1, i, j+1, seen): return True
                if bt(l+1, i, j-1, seen): return True
                if bt(l+1, i+1, j, seen): return True
                seen.discard((i,j))
            return False

        for i in range(R):
            for j in range(C):
                if board[i][j]==word[0]:
                    if bt(0, i, j): return True
        return False