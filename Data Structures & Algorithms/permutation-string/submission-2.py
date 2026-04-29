from collections import defaultdict
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        check1 = Counter(s1)
        check2 = defaultdict(int)
        window = len(s1)
        L = 0
        for R in range(len(s2)):
            check2[s2[R]]+=1

            if R - L + 1 > window:
                check2[s2[L]]-=1
                if not check2[s2[L]]:
                    del check2[s2[L]]
                L+=1
            
            if check2 == check1:
                return True
            
        return False
            

                