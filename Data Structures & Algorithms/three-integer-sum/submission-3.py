class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = set()
        nums.sort(reverse=True)
        for i in range(n-2):
            l = i +1 
            r = n-1
            while l < r:
                if nums[l] + nums[r] < -nums[i]:
                    r-=1
                elif nums[l] + nums[r] > -nums[i]:
                    l+=1
                else:
                    ans.add((nums[i], nums[r], nums[l]))
                    l+=1
                    r-=1
                    # break
        
        return list(ans)
                