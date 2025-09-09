from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        left_pointer = 9
        right_pointer = len(nums) - 1
        combinations = []
        seen = set()
        Onums = sorted(nums)

        for i in range(len(Onums)-1):
            target = 0 + Onums[i]

            left_pointer = i+1
            right_pointer = len(Onums) - 1

            if Onums[i] not in seen:

                while Onums[i] + Onums[left_pointer] + Onums[right_pointer] < 0 and left_pointer != right_pointer:
                    left_pointer += 1

                while Onums[i] + Onums[left_pointer] + Onums[right_pointer] > 0 and left_pointer != right_pointer:
                    right_pointer -= 1
            
            if Onums[i] + Onums[left_pointer] + Onums[right_pointer] == 0 and left_pointer != right_pointer:
                combinations.append([Onums[i],Onums[left_pointer],Onums[right_pointer]])


            seen.add(Onums[i])
        
        return combinations

nums = [-1,0,1,2,-1,-4]
    
sol = Solution()
print(sol.threeSum(nums))