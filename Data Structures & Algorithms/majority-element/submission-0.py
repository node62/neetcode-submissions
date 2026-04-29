class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        maj_ele = nums[0]
        maj_vote = 1        
        for i in range(1, len(nums)):
            if maj_vote > 0 and nums[i] != maj_ele:
                maj_vote -= 1
            elif maj_vote == 0 and nums[i] != maj_ele:
                maj_ele = nums[i]
                maj_vote += 1
            else:
                maj_vote += 1
        return maj_ele
            