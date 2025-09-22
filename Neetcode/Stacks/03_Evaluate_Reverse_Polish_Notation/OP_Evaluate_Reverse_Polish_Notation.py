from typing import List
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        # Recorro el array y guardo los numeros en mi stack
        # Al encontrar una operacion, aplico la operacion a los ultimos dos values de mi stack
        # guardo el resultado en el stack
        # Sigo iterando

        stack = []

        for token in tokens:
            if token not in "+-*/":
                stack.append(int(token))
            else:
                num2 = stack.pop()
                num1 = stack.pop()

                if token == '+':
                    stack.append(num1 + num2)

                elif token == '-':
                    stack.append(num1 - num2)

                elif token == '*':
                    stack.append(num1 * num2)

                elif token == '/':
                    stack.append(int(num1 / num2))

        return stack.pop()
    
tokens=["10","6","9","3","+","-11","*","/","*","17","+","5","+"]

sol = Solution()
print(sol.evalRPN(tokens))