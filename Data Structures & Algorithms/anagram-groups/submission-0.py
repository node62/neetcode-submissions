class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for s in strs:
            t = "".join(sorted(s))
            if t in d:
                d[t].append(s)
            else:
                d[t] = []
                d[t].append(s)
        ans = []
        for key in d:
            ans.append(d[key])
        
        return ans

              