import heapq
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # Crear un Hash Map con las frecuencias
        # Crear un heap de k espacios
        # Iterar sobre las keys e ir haciendo push:
            # siempre y cuando la key actual tenga un value mayor al heap[0], valor menor del heap
        
        # Frequency Hash
        freqs = Counter(nums)

        # Min Heap para guardar valor y frecuencia
        heap = []

        for key, freq in freqs.items():

            heapq.heappush(heap, (freq, key))

            # Si el size de mi heap es mayor a k, debo sustituir:
                # debo sustituir
            if len(heap) > k:
                heapq.heappop(heap)

        # Extraer los values
        return [key for freqs, key in heap]
    

nums = [1,1,1,2,2,3]
k = 2

sol = Solution()

print(Solution.topKFrequent(nums, k))