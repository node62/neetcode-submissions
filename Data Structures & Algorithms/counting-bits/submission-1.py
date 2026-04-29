class Solution:
    def countBits(self, n: int) -> List[int]:
        def hammingWeight(n: int) -> int:
            cnt = 0
            while n:
                if n & 1:
                    cnt+=1
                n>>=1
            return cnt
        
        ans = []
        for i in range(n+1):
            ans.append(hammingWeight(i))
        return ans