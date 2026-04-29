class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while True:
            seen.add(n)
            n = check(n)
            if n == 1:
                return True
            if n in seen:
                return False
    
def check(n):
    temp = 0
    while n:
        n, rem = divmod(n, 10)
        temp += rem**2
    print(temp)
    return temp