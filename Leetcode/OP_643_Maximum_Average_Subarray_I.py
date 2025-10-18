from typing import List

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        curr_sum = 0

        # First Window Average
        for i in range(k):
            curr_sum += nums[i]

        max_avg = curr_sum / k

        # Look for a bigger Average
        for i in range(k,len(nums)):
            curr_sum += nums[i]
            curr_sum -= nums[i-k]

            avg = curr_sum / k           
            max_avg = max(max_avg, avg)
            
        return max_avg

nums = [1,12,-5,-6,50,3]
k = 4

sol = Solution()
print(sol.findMaxAverage(nums,k))