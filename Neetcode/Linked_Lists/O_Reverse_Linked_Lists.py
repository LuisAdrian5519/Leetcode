class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # técnica de inversión iterativa que recorre la lista una sola vez, usando tres 
            # punteros (prev, curr, nxt) para deshacer el enlace y volver a conectarlo en 
            # la dirección opuesta.
        prev, curr = None, head

        while curr:
            # Guarda el Siguiente: Antes de romper el enlace de curr, guardamos dónde 
            # estaba apuntando en una variable temporal nxt.
            nxt = curr.next
            # El enganche (next) del nodo actual (curr) ya no apunta hacia adelante, sino 
            # hacia atrás, al nodo que acabamos de invertir (prev).
            curr.next = prev
            # El nodo actual (curr) ya terminó su trabajo y está perfectamente apuntando hacia 
            # atrás. Lo convertimos en el nuevo nodo "previo" para el siguiente ciclo.
            prev = curr
            # Movemos el puntero curr al siguiente nodo de la cadena original, usando el enlace 
            # que guardamos en la variable nxt
            curr = nxt

        return prev
    

head = [0,1,2,3]
sol = Solution()
print(sol.reverseList)
