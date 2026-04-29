from collections import defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        ds = defaultdict(int)
        dt = defaultdict(int)
        for c in t:
            dt[c]+=1
        
        def check():
            for k, v in dt.items():
                if v > 0 and ds[k] < v:
                    print(False)
                    return False
                print(True)
            return True
        
        L = 0
        minl = float('inf')
        finR = 0
        finL = 0
        for R in range(len(s)):
            ds[s[R]]+=1
            while check():
                size = R - L + 1
                if size < minl:
                    minl = size
                    print(minl)
                    finR = R
                    finL = L
                ds[s[L]]-=1
                L+=1
        
        return s[finL: finR+1] if minl != float('inf') else ""