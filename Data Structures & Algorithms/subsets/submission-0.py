class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        fin = []
        def helper(ip, op=[]):
            if not ip:
                fin.append(op)
                return 
            first = ip[0]
            ip = ip[1:]
            op1 = op + [first]
            op2 = op
            helper(ip, op1)
            helper(ip, op2)
            return 
        helper((nums))
        return fin