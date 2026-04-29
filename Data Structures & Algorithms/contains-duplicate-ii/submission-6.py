# hash set approach
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        seen = set()

        L = 0 
        for R in range(n):

            # if R - L >= k:
            #     seen.remove(nums[L])
            #     L+=1

            if nums[R] in seen:
                return True
            
            seen.add(nums[R])
        
            '''
            if you are checking for window length after checking the condition, you should 
            see if the window length is equal to the fixed length, not greater than.
            '''       
            if R - L == k:
                seen.remove(nums[L])
                L+=1

        return False
        
