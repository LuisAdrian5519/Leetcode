class Solution(object):
    def removeSubstring(self, s, k):

        # Puedo stackear los open y cuando salga un closed, eliminarlo del stack
        # Y luego reconstuir mi output con los parentesis sobrantes? Pero como se el orden

        stack = []
        open_counter = 0
        closed_counter = 0
        
        for char in range(len(s)):
            if s[char] == '(':
                if stack and stack[-1] == ')':
                    open_counter = 0
                stack.append(s[char])
                open_counter += 1
            else:
                stack.append(s[char])
                closed_counter += 1

            if open_counter >= k and closed_counter >= k:
                for i in range(k*2):
                    if stack.pop() == '(':
                        open_counter -= 1
                    else:
                        closed_counter -= 1

        return "".join(stack)

    

s = "((()))()()()"
k = 3

sol = Solution()

# Llama a la función con los argumentos
print(sol.removeSubstring(s,k)) 