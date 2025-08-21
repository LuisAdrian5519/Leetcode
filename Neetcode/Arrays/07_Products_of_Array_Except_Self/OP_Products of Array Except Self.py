class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
      
        n = len(nums)
        output = [1]*n
        # [1,2,3,4]

        prefix_product = 1
        for i in range(n):
            output[i] = prefix_product
            prefix_product *= nums[i]

        # output = [1,1,2,6]

        suffix_product = 1
        for i in range(n-1,-1,-1):
            output[i] *= suffix_product
            suffix_product *= nums[i]

        # output = [24,12,8,6]    

        return output