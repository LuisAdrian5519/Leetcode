from typing import List
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        # Recorro el array y guardo los numeros en mi stack
        # Al encontrar una operacion, aplico la operacion a los ultimos dos values de mi stack
        # guardo el resultado en el stack
        # Sigo iterando

        stack = []
        num1 = 0
        num2 = 0
        res = 0

        for token in tokens:
            try:
                Ntoken = int(token)
                stack.append(Ntoken)

            except ValueError:
                if token == '+':
                    num1 = stack[-1]
                    stack.pop()
                    num2 = stack[-1]
                    stack.pop()
                    res = num1 + num2
                    stack.append(res)

                elif token == '-':
                    num1 = stack[-1]
                    stack.pop()
                    num2 = stack[-1]
                    stack.pop()
                    res = num2 - num1
                    stack.append(res)

                elif token == '*':
                    num1 = stack[-1]
                    stack.pop()
                    num2 = stack[-1]
                    stack.pop()
                    res = num1 * num2
                    stack.append(res)

                elif token == '/':
                    num1 = stack[-1]
                    stack.pop()
                    num2 = stack[-1]
                    stack.pop()
                    res = int(num2 / num1)
                    stack.append(res)

        return stack[-1]

tokens=["10","6","9","3","+","-11","*","/","*","17","+","5","+"]

sol = Solution()
print(sol.evalRPN(tokens))