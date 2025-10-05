from typing import List
import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        # BRUTE FORCE        
        # Tenemos un array de pilas de bananas, debo elegir un eating rate minimo para poder comerlas 
            # dentro del tiempo establecido
        # Debo buscar el numero minimo que pueda dividir al resto en un numero de operaciones menor a h
        # No importa el indice, así que puedo hacer un sort
        # Despues del sort, puedo hacer un ciclo que para cada valor, cuente las operaciones que toma
            # el dividir los numeros del array hasta que el modulo sea 0 y ver si ese num es menor a h
        # Nota: No tengo que elegir un valor para k dentro de los values de la pila

        # OPTIMAL
        # Debo buscar el numero minimo que pueda dividir al resto en un numero de operaciones menor a h
        # No importa el indice, así que puedo hacer un sort
        # 

        l, r = 1, max(piles)
        # Ar least the max number in piles is the solution
        res = r

        while l <= r:
            k = (l + r) // 2
            
            hours = 0
            for p in piles:
                # Redondear el resultado hacia arriba
                hours += math.ceil(float(p)/k)
            if hours <= h:
                res = min(res,k)
                r = k-1
            else:
                l = k+1 

        return l
    
piles = [1,4,3,2]
h = 9
    
sol = Solution()
print(sol.minEatingSpeed(piles, h))