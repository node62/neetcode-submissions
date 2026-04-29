class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        some = set()
        for num in nums:
            if num in some:
                return True
            some.add(num)
        return False