from typing import List

class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        n = len(nums)
        max_length = 0

        # El bucle externo define el punto de inicio 'i' del sub-arreglo
        for i in range(n):
            
            # Inicializamos los conjuntos para cada nuevo sub-arreglo que empieza en 'i'
            distinct_even = set()
            distinct_odd = set()
            
            # El bucle interno define el punto final 'j' del sub-arreglo
            # El sub-arreglo es nums[i:j+1]
            for j in range(i, n):
                
                # 1. Clasificar el número actual (nums[j])
                current_num = nums[j]
                
                if current_num % 2 == 0:
                    # El número es par, lo agregamos al set de pares
                    distinct_even.add(current_num)
                else:
                    # El número es impar, lo agregamos al set de impares
                    distinct_odd.add(current_num)
                
                # 2. Verificar la condición de "Balanced"
                # Contamos la cantidad de números distintos en cada set
                count_even = len(distinct_even)
                count_odd = len(distinct_odd)
                
                # Si las cantidades son iguales, el sub-arreglo es Balanced
                if count_even == count_odd:
                    # 3. Actualizar la longitud máxima
                    # La longitud del sub-arreglo actual es (j - i + 1) AQUI SE CONSIDERAN LOS DUPLICADOS
                    current_length = j - i + 1
                    max_length = max(max_length, current_length)
        
        return max_length

nums = [7,7,10,4]

sol = Solution()
print(sol.longestBalanced(nums))
    
