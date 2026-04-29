from collections import defaultdict
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        perm = Counter(s1)
        check = defaultdict(int)
        win = len(s1)
        L = 0
        for R in range(len(s2)):
            check[s2[R]]+=1

            if R - L + 1 > win:
                check[s2[L]]-=1
                if not check[s2[L]]:
                    del check[s2[L]]
                L+=1
            
            if check == perm:
                return True
            
        return False
            

                