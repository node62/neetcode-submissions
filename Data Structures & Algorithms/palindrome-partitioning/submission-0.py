class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        cur = []
        fin = []
        def is_pal(word):
            for i in range(len(word)//2):
                if word[i] != word[~i]:
                    return False
            return True
        def backtrack(i):
            if i == n:
                fin.append(cur[:])
                return
            
            for j in range(i, n):
                temp = s[i:j+1]
                if is_pal(temp):
                    cur.append(temp)
                    backtrack(j+1)
                    cur.pop()
        backtrack(0)
        return fin