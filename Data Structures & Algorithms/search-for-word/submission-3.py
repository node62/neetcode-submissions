class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        R = len(board)
        C = len(board[0])
        def increment(i, j):
            if j == C-1:
                i += 1
                j = 0
            else:
                j+=1
            return i, j            
        
        ans = False
        def bt(l, i, j, seen=set()):
            nonlocal ans
            if l == len(word):
                ans = True
                return
            if ans or not 0<=i<R or not 0<=j<C:
                return 
            if word[l] == board[i][j] and \
            (i, j) not in seen:
                seen.add((i, j))
                bt(l+1, i-1, j, seen)                
                bt(l+1, i, j+1, seen)
                bt(l+1, i, j-1, seen)
                bt(l+1, i+1, j, seen)
                seen.discard((i,j))
        for i in range(R):
            for j in range(C):
                if board[i][j]==word[0]:
                    bt(0, i, j)
                if ans: return ans
        return ans