class Solution:
    def calPoints(self, op: List[str]) -> int:
        stack = []        
        for v in op:
            if v == '+':
                stack.append(stack[-1] + stack[-2])
            elif v == 'D':
                stack.append(2*stack[-1])
            elif v == 'C':
                stack.pop()
            else:
                stack.append(int(v))
        return sum(stack)
