from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        numap = {}
        
        for i, num in enumerate(nums):
            
            z = target - num

            if z in numap:
                return [numap[z], i] # [numap[z] == j, i]          
            numap[num] = i

        return []

nums=[1,3,4,2]
target=6

Solution = Solution()
print(Solution.twoSum(nums, target))