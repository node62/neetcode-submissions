class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        max_ele, arr[~0] = arr[~0], -1
        for i in range(1, len(arr)):
            temp = arr[~i]
            arr[~i] = max_ele
            if max_ele < temp: max_ele = temp
        return arr
            
