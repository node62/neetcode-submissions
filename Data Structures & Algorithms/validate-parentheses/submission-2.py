class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        value = {
            ']':'[',
            ')':'(',
            '}':'{'
        }

        for i in s:
            if i in value.values():
                stack.append(i)
            elif i in value.keys():
                if not stack or value[i] != stack.pop():
                    return False
        
        return not stack
                
            

