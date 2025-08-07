class Solution:
    def twoSum(self, nums, target):

        for i in range(len(nums)):

            complement = target - nums[i]

            for j in range(i, len(nums)-1):

                if nums[j] == complement:

                    return [i,j]
                

nums = [4,5,6]
target = 10

# 1. Crea una instancia de la clase Solution
solution_instance = Solution()

# 2. Llama al método twoSum usando la instancia
result = solution_instance.twoSum(nums, target)

print(result)