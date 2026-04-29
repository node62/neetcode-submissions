class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for v in nums:
            if v not in d:
                d[v] = 1
            else:
                d[v] += 1
        
        sorted_list = sorted(d.items(), key= lambda x:x[1])
        ans = []
        for i in range(len(sorted_list)-k, len(sorted_list)):
            ans.append(sorted_list[i][0])
        return ans

