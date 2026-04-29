class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        def put(c, arr, n):
            if ord('A') <= ord(c) <= ord('Z'):
                arr[ord(c) - ord('A')] += n
            elif ord('a') <= ord(c) <= ord('z'):
                arr[ord(c) - ord('a') + 26]+=n

        def check():
            for i in range(len(lt)):
                if lt[i] > 0 and lt[i] > ls[i]:
                    return False
            return True
                
        ls = [0] * 52
        lt = [0] * 52
        for c in t:
            put(c, lt, 1)
        
        L = 0
        minl = float('inf')
        finR = 0
        finL = 0
        for R in range(len(s)):
            put(s[R], ls, 1)
            while check():
                size = R - L + 1
                if size < minl:
                    minl = size
                    finR = R
                    finL = L
                put(s[L], ls, -1)                                  
                L+=1
        
        return s[finL: finR+1] if minl != float('inf') else ""
            
            
        