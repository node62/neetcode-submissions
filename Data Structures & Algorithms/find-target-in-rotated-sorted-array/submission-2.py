class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        low, high = 0, n-1

        while low <= high:
            mid = (low + high) // 2
            mv = nums[mid]
            lv = nums[low]
            hv = nums[high]

            if mv == target:
                return mid

            if mv <= hv:
                if hv >= target > mv:
                    low = mid + 1
                else:
                    high = mid - 1
                    
            else:
                if lv <= target < mv:
                    high = mid - 1
                else:
                    low = mid + 1

        return -1
