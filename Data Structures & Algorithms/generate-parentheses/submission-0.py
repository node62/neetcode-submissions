class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        fin = []
        cur = []
        def bt(open=n, close=n):
            if not open and not close:
                fin.append("".join(cur))
                return

            elif open == close:
                cur.append('(')            
                bt(open-1, close)
                cur.pop()

            elif open and open < close:
                cur.append('(')
                bt(open-1, close)
                cur.pop()

                cur.append(')')
                bt(open, close - 1)
                cur.pop()
            elif not open:
                cur.append(')')
                bt(open, close-1)
                cur.pop()
        bt()
        return fin
