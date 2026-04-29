class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 1
        right = len(numbers)

        while left < right:
            a = numbers[left - 1]
            b = numbers[right - 1]

            if a + b > target:
                right -=1
            
            elif a + b < target:
                left +=1

            elif a + b == target:
                return [left, right]

