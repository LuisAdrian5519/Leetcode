from typing import List

class Solution:
    def maxArea(self, heights: List[int]) -> int:

        left_pointer = 0
        right_pointer = len(heights) - 1
        increment_left = 1
        increment_right = 1

        while left_pointer < right_pointer:
            container = min(heights[left_pointer],heights[right_pointer]) * abs(right_pointer - left_pointer)

            if heights[left_pointer] < heights[right_pointer]:
                if heights[left_pointer] < heights[left_pointer + increment_left]:
                    left_pointer += increment_left
                else:
                    increment_left += 1

            elif heights[left_pointer] > heights[right_pointer]:
                if heights[right_pointer] < heights[right_pointer - increment_right]:
                    right_pointer -= increment_right
                else:
                    increment_right += 1

            else:
                return container

        return container 
    
height = [1,7,1,1,1,1,2,5,12,3,500,50,7,8,4,7,38,9,10,12,6]

sol = Solution()

print(sol.maxArea(height))