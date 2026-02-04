from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
    
        while l <= r:
            m = (l + r) // 2
        
            # Caso base: encontramos el target
            if nums[m] == target:
                return m
        
            # Determinar qué lado está ordenado
            if nums[l] <= nums[m]:  # Lado IZQUIERDO ordenado
                # ¿El target está en este rango ordenado?
                if nums[l] <= target < nums[m]:
                    r = m - 1  # Buscar en la izquierda
                else:
                    l = m + 1  # Buscar en la derecha
        
            else:  # Lado DERECHO ordenado
                # ¿El target está en este rango ordenado?
                if nums[m] < target <= nums[r]:
                    l = m + 1  # Buscar en la derecha
                else:
                    r = m - 1  # Buscar en la izquierda
    
        return -1  # No encontrado


sol = Solution()
print(sol.search(nums = [4,5,6,7,0,1,2], target = 6))