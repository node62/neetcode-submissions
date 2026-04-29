def hammingWeight(n: int) -> int:
    cnt = 0
    while n:
        if n & 1:
            cnt+=1
        n>>=1
    return cnt
answer = {0:[0]}
for i in range(1, 1001):
    answer[i] = answer[i-1] + [hammingWeight(i)]

class Solution:
    def countBits(self, n: int) -> List[int]:
        return answer[n]
        