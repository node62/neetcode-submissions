class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        phone = {
            "2": "abc", 
            "3": "def", 
            "4": "ghi",
            "5": "jkl",
            "6": "mno", 
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        fin = []
        def helper(i, cur = ''):
            if len(cur) == len(digits):
                if cur: fin.append(cur)
                return 
            for c in phone[digits[i]]:
                helper(i+1, cur + c)
        helper(0)
        return fin

                

        