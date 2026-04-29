class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        pre = [0] * (n+1)
        hist = {0:1}
        ans = 0

        for i in range(n):
            pre[i+1] = pre[i] + nums[i]
            lookup = pre[i+1] - k
            if lookup  in hist:
                ans+= hist[lookup]

            if pre[i+1] not in hist:
                hist[pre[i+1]] = 1
            else:
                hist[pre[i+1]]+=1
        
        return ans
