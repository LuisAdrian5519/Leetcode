from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        # Solo necesitamos validar filas y columnas, no saber si el sudoku se puede resolver 
        # No duplicates en squares

        s = {'1', '2', '3', '4', '5', '6', '7', '8', '9'}

        # No duplicates in rows:
        for row in board:
            seen = set()

            for num in row:
                if num in s:
                    if num in seen:
                        return False
                    seen.add(num)

        # No duplicates in columns:
        for col in range(len(board[0])):

            seen = set()

            for row in range(len(board)):
                num = board[row][col]
                if num in s:
                    if num in seen:
                        return False
                    seen.add(num)

        # No duplicates en squares
        for box_row in range(3):
            for box_col in range(3):

                seen = set()

                for i in range(3):
                    for j in range(3):
                        
                        #Calcular las posiciones reales
                        row = box_row * 3 + i
                        col = box_col * 3 + j
                        num = board[row][col]

                        if num in s:
                            if num in seen:
                                return False
                            seen.add(num)

        return True

board = [["5","3",".",".","7",".",".",".","."]
        ,["6",".",".","1","9","5",".",".","."]
        ,[".","9","8",".",".",".",".","6","."]
        ,["8",".",".",".","6",".",".",".","3"]
        ,["4",".",".","8",".","3",".",".","1"]
        ,["7",".",".",".","2",".",".",".","6"]
        ,[".","6",".",".",".",".","2","8","."]
        ,[".",".",".","4","1","9",".",".","5"]
        ,[".",".",".",".","8",".",".","7","9"]]

sol = Solution()

print(sol.isValidSudoku(board))