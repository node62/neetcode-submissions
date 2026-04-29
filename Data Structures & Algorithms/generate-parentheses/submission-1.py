class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        fin = []        
        cur = []
        def bt(open, close):
            if not open and not close:
                fin.append("".join(cur))
                return
            if open:
                cur.append('(')
                bt(open-1, close)
                cur.pop()
            if close > open:
                cur.append(')')
                bt(open, close-1)
                cur.pop()
        bt(n, n)
        return fin
            