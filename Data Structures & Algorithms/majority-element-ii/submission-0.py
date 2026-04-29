class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        limit = n//3
        cnt = Counter(nums)
        ans = []
        for k, v in cnt.items():
            if v > limit:
                ans.append(k)
        return ans
