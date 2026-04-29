class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits: return []        
        digit2char = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }
        fin = []
        def bt(i, cur=""):
            if len(cur)==len(digits):
                fin.append(cur)
                return
            str2consider = digit2char[digits[i]]
            for c in str2consider:
                bt(i+1, cur + c)
        
        bt(0)
        return fin