from collections import defaultdict
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        window = len(s1)
        check1 = [0] * 26
        for c in s1:
            check1[ord(c) - ord('a')]+=1

        check2  =[0] * 26
        L = 0
        for R in range(len(s2)):
            check2[ord(s2[R]) - ord('a')]+=1

            if R - L + 1 > window:
                check2[ord(s2[L]) - ord('a')]-=1
                L+=1
            
            if check2 == check1:
                return True
            
        return False