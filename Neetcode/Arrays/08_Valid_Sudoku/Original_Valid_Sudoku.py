from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        filas = [set() for _ in range(9)]
        columnas = [set() for _ in range(9)]
        cajas = [set() for _ in range(9)]

        for r in range(9):
            for c in range(9):
                num = board[r][c]
                if num == ".":
                    continue
                
                caja_indice = (r // 3) * 3 + c // 3

                if num in filas[r] or num in columnas[c] or num in cajas[caja_indice]:
                    return False

                filas[r].add(num)
                columnas[c].add(num)
                cajas[caja_indice].add(num)

            return True
