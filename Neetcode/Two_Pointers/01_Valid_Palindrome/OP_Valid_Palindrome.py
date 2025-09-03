class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Punteros para los extremos de la cadena original
        left_pointer, right_pointer = 0, len(s) - 1

        while left_pointer < right_pointer:
            # Mover el puntero izquierdo si no es alfanumérico
            while left_pointer < right_pointer and not s[left_pointer].isalnum():
                left_pointer += 1
            
            # Mover el puntero derecho si no es alfanumérico
            while left_pointer < right_pointer and not s[right_pointer].isalnum():
                right_pointer -= 1

            # Comparar los caracteres alfanuméricos
            if s[left_pointer].lower() != s[right_pointer].lower():
                return False

            # Mover ambos punteros hacia el centro
            left_pointer += 1
            right_pointer -= 1

        return True
    
s = "Madam, in Eden, I'm Adam"
    
sol = Solution()
print(sol.isPalindrome(s))