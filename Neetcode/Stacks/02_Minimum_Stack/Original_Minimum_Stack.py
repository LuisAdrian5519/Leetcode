class MinStack:
    # Stack que soporta operaciones de push, pop, top y getMin (O(1)).
    
    def __init__(self):
        # Inicia el Stack principal y el stack auxiliar para el mínimo
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        # Agrega un elemento a la pila.
        # Actualiza el auxiliar stack si está vacío o si el nuevo valor es menos a su Top.
        self.stack.append(val)
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)
        

    def pop(self) -> None:
        # Elimina el elemento superior de la pila.
        # Si el elemento eliminado es el mínimo actual, también lo elimina de la
        # pila auxiliar del mínimo.
        if self.stack:
            popped_val = self.stack.pop()
            if popped_val == self.min_stack[-1]:
                self.min_stack.pop()
        else:
            raise IndexError("La pila está vacía")
        

    def top(self) -> int:
        # Devuelve el elemento superior del stack sin eliminarlo.
        if not self.stack:
            raise IndexError("La pila está vacía")
        return self.stack[-1]
        

    def getMin(self) -> int:
        # Devuelve el elemento mínimo en el stack.
        # Esta operación es de tiempo constante (O(1)).
        if not self.min_stack:
            raise IndexError("La pila está vacía")
        return self.min_stack[-1]


minStack = MinStack()
minStack.push(2)
minStack.push(1)
minStack.pop()
print(minStack.top())
print(minStack.getMin())