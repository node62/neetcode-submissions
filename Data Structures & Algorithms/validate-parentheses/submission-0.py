class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        value = {
            '(':0, 
            ')':0,
            '[':1,
            ']':1,
            '{':2,
            '}':2
        }

        for i in s:
            if i in "[({":
                stack.append(value[i])
            else:
                if not stack:
                    return False
                
                top = stack.pop()

                if value[i] != top:
                    return False
        
        if stack:
            return False
        return True
                
            

