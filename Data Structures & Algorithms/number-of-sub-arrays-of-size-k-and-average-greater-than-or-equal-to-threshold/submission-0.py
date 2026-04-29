# queue implementation
class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        curr_sum = 0
        res = 0

        L = 0
        for R in range(len(arr)):
            curr_sum += arr[R]

            win_size = R-L+1
            if win_size > k:
                curr_sum -= arr[L]
                L+=1
                
            win_size = R-L+1

            curr_avg = (curr_sum // win_size)

            if curr_avg >= threshold and win_size == k:
                res +=1
        
        return res
            
