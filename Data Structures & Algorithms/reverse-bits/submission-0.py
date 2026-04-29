class Solution:
    def reverseBits(self, n: int) -> int:
        m = 0
        for i in range(32):
            t = n&1
            n>>=1
            m<<=1
            m = m|t
        return m
        