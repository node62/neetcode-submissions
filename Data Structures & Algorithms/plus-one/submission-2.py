class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        fun = lambda x: str(x)
        num = int("".join(map(fun, digits)))
        num+=1
        return [int(x) for x in str(num)]
        