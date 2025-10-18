from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:

        l,r = 0, len(nums)-1
        res = nums[0]

        while l <= r:
            # Already sorted array:
            if nums[l] < nums[r]:
                res = min(res,nums[l])
                break

            m = (l + r) // 2
            res = min(res,nums[m])
            
            if nums[m] >= nums[l]:
                # Search Right
                l = m + 1
            else:
                # Search left
                r = m - 1 

        return res

nums = []

sol = Solution()
print(sol.findMin(nums))