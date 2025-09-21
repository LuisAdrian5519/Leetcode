class Solution:
    def isValid(self, s: str) -> bool:
        
        # Ir guardando los brackets de apertura en un stack
        # Al encontrar uno de cerradura, comprobar que sea del mismo tipo que el peek en el stack, si no, FALSE
        # Si, si es igual, le hacemos pop() al stack

        stack = []

        if len(s) <= 1:
            return False

        for bracket in s:
            if bracket == "[" or bracket == "(" or bracket == "{":
                stack.append(bracket)
            elif bracket == "]":
                if stack == []:
                    return False
                elif "[" == stack[-1]:
                    stack.pop()
                else:
                    return False
            elif bracket == ")":
                if stack == []:
                    return False
                if "("== stack[-1]:
                    stack.pop()
                else:
                    return False
            elif bracket == "}":
                if stack == []:
                    return False
                if "{" == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                pass

        if stack == []:
            return True
        else:
            return False