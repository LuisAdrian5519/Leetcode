class Solution:
    def isPalindrome(self, s: str) -> bool:

        s = "".join(char for char in s if char.isalnum())
        condensed_s = s.lower()

        right_pointer = len(condensed_s) - 1
        
        for left_pointer in range(len(condensed_s)):            
            if left_pointer == right_pointer or left_pointer >= right_pointer:
                return True

            if condensed_s[left_pointer] != condensed_s[right_pointer]:
                return False

            right_pointer -= 1
        
        return True