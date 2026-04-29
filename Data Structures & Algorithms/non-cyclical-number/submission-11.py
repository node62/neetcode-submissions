class Solution:
    def isHappy(self, n: int) -> bool:
        slow, fast = n, fun(n)
        while fast!=1:
            print(slow, fast)
            slow = fun(slow)    
            fast = fun(fun(fast)) 
            if fast == slow:
                return False
        return True
    
def fun(n):
    temp = 0
    while n:
        n, rem = divmod(n, 10)
        temp += rem**2
    return temp