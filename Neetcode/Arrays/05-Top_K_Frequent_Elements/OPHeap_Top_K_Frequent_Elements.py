import heapq

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        # Paso 1: Usar tu función arr2hash para obtener el conteo de frecuencias
        freq_map = self.arr2hash(nums)

        min_heap = []
        
        # Iterar sobre los elementos del diccionario de frecuencias
        for num, freq in freq_map.items():
            heapq.heappush(min_heap, (freq, num))
            
            if len(min_heap) > k:
                heapq.heappop(min_heap)
        
        # Paso 3: Extraer los k elementos más frecuentes del heap
        result = []
        while min_heap:
            freq, num = heapq.heappop(min_heap)
            result.append(num)
        
        return result

    def arr2hash(self, array):
        hashmap = {}
        for char in array:
            if char not in hashmap:
                hashmap[char] = 1
            else:
                hashmap[char] += 1
        return hashmap