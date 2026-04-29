import math
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        n = len(tokens)
        stack = []
        for i, v in enumerate(tokens):
            if v not in "+-*/":
                stack.append(int(v))
            else:
                match v:
                    case '+':
                        num2 = stack.pop()
                        num1 = stack.pop()
                        stack.append(num1 + num2)
                    case '-':
                        num2 = stack.pop()
                        num1 = stack.pop()
                        stack.append(num1 - num2)
                    case '*':
                        num2 = stack.pop()
                        num1 = stack.pop()
                        stack.append(num1 * num2)
                    case '/':
                        num2 = stack.pop()
                        num1 = stack.pop()
                        ans = num1 / num2
                        if ans < 0:
                            stack.append(math.ceil(ans))
                        else:
                            stack.append(math.floor(ans))

        return stack.pop()