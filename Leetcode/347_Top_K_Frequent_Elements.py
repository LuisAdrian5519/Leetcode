import heapq
from collections import Counter

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        
        # Crear un Hash Map con las frecuencias
        # Crear un heap de k espacios
        # Iterar sobre las keys e ir haciendo push:
            # siempre y cuando la key actual tenga un value mayor al heap[0], valor menor del heap
        
        freq = Counter(nums)

        heap = [0] * k

        for key in freq.keys():
            # Si tengo un número cuya frecuencia es igual a la frecuencia más baja de mi heap:
                # debo sustituir
            if freq[key] > heap[0]:
                heapq.heappop(heap)
                heapq.heappush(heap, key)

        return heap
    

nums = [1,1,1,2,2,3]
k = 2

sol = Solution()

print(Solution.topKFrequent(nums, k))