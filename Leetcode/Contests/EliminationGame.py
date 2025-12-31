class Solution(object):
    def lastRemaining(self, n):
        """
        :type n: int
        :rtype: int
        """
        # En lugar de mantener el array, solo trackeamos:
        # - head: el primer elemento que queda
        # - remaining: cuántos elementos quedan
        # - step: la distancia entre elementos consecutivos
        
        head = 1
        remaining = n
        step = 1
        left_to_right = True
        
        while remaining > 1:
            # Actualizamos head si:
            # 1. Vamos de izquierda a derecha (siempre eliminamos el primero)
            # 2. O vamos de derecha a izquierda CON número impar de elementos
            if left_to_right or remaining % 2 == 1:
                head += step
            
            # Después de cada pasada:
            remaining //= 2  # Se elimina la mitad
            step *= 2        # La distancia se duplica
            left_to_right = not left_to_right  # Cambiamos dirección
        
        return head

n = 9
sol = Solution()

# Test 1
print(sol.lastRemaining(9))  # Output: 6