class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        result = 1
        output = [0]*len(nums)

        for i in range(len(nums)):
            for j in range(len(nums)):
                if j != i:
                    result = nums[j] * result
            output[i] = result
            result = 1
        

        return output

            
