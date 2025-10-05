from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        # Podemos iterar a traves del primer indice de cada fila de la matrix
        # Preguntamos si es el numero, si es, retornamos
        # Hacemos busqueda binaria hasta quedar con una fila
        # Con una única fila, rehacemos binary search para esos valores

        l,r = 0, len(matrix)-1
        row = 0

        while l < r:

            row = (l + r) // 2

            if target > matrix[row][-1]:
                l = row + 1

            elif target < matrix[row][0]:
                r = row - 1

            else:
                break

        row = (l + r) // 2

        l,r = 0, len(matrix[0])-1
        column = 0

        while l <= r:

            column = (l + r) // 2

            if target > matrix[row][column]:
                l = column + 1

            elif target < matrix[row][column]:
                r = column - 1

            else:
                return True

        return False
    
matrix=[[1,3,5,7],[10,11,16,20],[23,30,34,50]]
target=11

sol = Solution()
print(sol.searchMatrix(matrix,target))