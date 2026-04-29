class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = int("".join(map(str, digits)))
        num+=1
        num = list(str(num))
        digits = map(int, num)
        return list(digits)
        