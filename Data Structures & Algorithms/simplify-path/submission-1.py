class Solution:
    def simplifyPath(self, path: str) -> str:
        realpath = ""
        tog = False
        for c in path:
            if c == '/' and tog == False: tog = True
            elif c == '/' and tog == True: continue
            elif c != '/': tog = False
            realpath += c
        print(realpath)
        realpath = realpath.split('/')
        print(realpath)
        stack = []
        for c in realpath:
            if c == '.' or c=='': continue
            elif c == '..':
                if stack: stack.pop() 
                continue
            stack.append(c)
        return '/' + '/'.join(stack)


