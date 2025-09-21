from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        
        acc = 0

        # Iterar con dos punteros, el right avanza hasta dar con un valor igual o mayor al de left
        # Se itera por cada valor entre left y right y se suma a un acumulador la altura del pointer menor 
            # menos el valor intermedio evaluado (lo que cabe de agua)
        # Se iguala left al valor de right y se vuelve a avanzar con right
        
        for i in range(1,len(height)-1):

            max_left = max(height[0:i])
            max_right = max(height[i:len(height)])

            res = min(max_left,max_right) - height[i]
            if res > 0:
                acc += res
            else:
                pass

        return acc
        # while l != len(height)-1:
            
        #     # Buscar con right_pointer una barra igual o mayor a mi barra actual, sin sobrepasar el final de mi lista
        #     while height[l] > height[r] or l == r:
        #         if r == len(height)-1:
        #             l+=1
        #             if l == len(height)-1:
        #                 return acc
        #             r=l
        #         else:
        #             r+=1

            
        #     for i in range(l,r):
        #         acc += min(height[l],height[r]) - height[i]

        #     # Acabado este ciclo For, i es igual a r, ahora debo igualar l al valor de r y volver a ciclar

        #     l = r
        
        # return acc
    
height=[4,2,3]
sol = Solution()

print(sol.trap(height))