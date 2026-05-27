class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        str2int = {f"{x}": x for x in range(10)}
        int2str = {x: f"{x}" for x in range(10)}
        a = b = 0
        for i in num1:
            a *= 10
            a += str2int[i]
        for i in num2:
            b *= 10
            b += str2int[i]
        mul = a*b
        if not mul: return "0"
        ans = []
        while mul:
            mul, rem = divmod(mul, 10)
            ans.append(int2str[rem])
        return "".join(reversed(ans))
        