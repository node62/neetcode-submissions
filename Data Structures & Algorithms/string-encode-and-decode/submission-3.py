class Solution:
    def encode(self, strs: List[str]) -> str:
        if not strs:
            return "0"
        l = []
        for s in strs:
            l.append(str(len(s)))
        A = ",".join(l)
        B = "".join(strs)
        return A + "#" + B

    def decode(self, s: str) -> List[str]:
        if s=="0":
            return []
        parts = s.split('#', 1)
        A = parts[0]
        B = parts[1]
        l = A.split(',')
        final = []
        j = 0
        for i in l:
            i = int(i)
            final.append(B[j:j+i])
            j = j+i
        return final

