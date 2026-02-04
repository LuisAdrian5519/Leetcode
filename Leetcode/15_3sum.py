from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        # Triple For loop O(n^3)
        # Si usamos Hash - Hash de frecuencias
        # Dos ciclos y generación de Target
        # Buscamos target en el Hash y hacemos append a res solo si
            # No es duplicate (diferente a i y j o frecuencia 2 o superior)

        # Qué pasa si hago sort?
        # puedo hacer un solo for y luego implementar two_sum II para el resto del array

        res = []
        nums.sort()

        for i, a in enumerate(nums):
            # Checamos que no sea duplicate a partir del 2nd element of list
            if i > 0 and a == nums[i-1]:
                continue

            # Use Two pointers to find the correct combination
            l, r = i + 1, len(nums) - 1

            while l < r:
                threesum = a + nums[l] + nums[r]
                if threesum > 0:
                    r -= 1
                elif threesum < 0:
                    l += 1
                else:
                    res.append([a,nums[l],nums[r]])
                    l += 1
        return res
    

nums = [-1,0,1,0]

sol = Solution()

print(sol.threeSum(nums))