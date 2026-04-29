class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

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

        prev_layer = ['']
        for d in digits:
            curr_layer = []
            for curStr in prev_layer:
                for c in digit2char[d]:
                    curr_layer.append(curStr + c)
            prev_layer = curr_layer
        
        return prev_layer
