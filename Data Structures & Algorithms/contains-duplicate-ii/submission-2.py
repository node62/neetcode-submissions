class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if not k:
            return False

        n = len(nums)
        win = []

        for L in range(n):
            for R in range(L+1, min(n, L+k+1)):
                if nums[L] == nums[R]:
                    return True
        
        return False