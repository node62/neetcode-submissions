class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        ans = []
        for i in range(n):
            l = 0
            t = True
            for j in range(i, n):
                if temperatures[j] > temperatures[i]:
                    t = False
                    break
                l+=1
            
            if t:
                l = 0
            
            ans.append(l)

        return ans