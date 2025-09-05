from collections import defaultdict

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        # 1. iterar sobre un numero i
        # 2. Generar una variable z = i - target
        # 3. Buscar en Hashmap del array

        RHash = self.arr2hash(numbers)

        for i in range(len(numbers)):
            z = target - numbers[i]
            if z in RHash.keys() and RHash[z] != i:
                return [i+1, RHash[z]+1]

    def arr2hash(self, arr):
        Hash = defaultdict(int)
        for i in range(len(arr)):
            Hash[arr[i]] = i

        return Hash

