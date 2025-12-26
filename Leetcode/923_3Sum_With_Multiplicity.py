class Solution(object):
    def threeSumMulti(self, arr, target):
        from collections import Counter
        
        MOD = 10**9 + 7
        count = Counter(arr)
        res = 0
        
        # Iterar sobre pares únicos de valores
        for i in count:
            for j in count:
                k = target - i - j  # El tercer número que necesitamos
                
                if k not in count:
                    continue
                
                # Caso 1: Tres números diferentes (i < j < k)
                if i < j < k:
                    res += count[i] * count[j] * count[k]
                
                # Caso 2: Dos números iguales (i == j < k)
                elif i == j < k:
                    res += count[i] * (count[i] - 1) // 2 * count[k]
                
                # Caso 3: Dos números iguales (i < j == k)
                elif i < j == k:
                    res += count[i] * count[j] * (count[j] - 1) // 2
                
                # Caso 4: Tres números iguales (i == j == k)
                elif i == j == k:
                    res += count[i] * (count[i] - 1) * (count[i] - 2) // 6
        
        return res % MOD
    

arr = [1,1,2,2,3,3,4,4,5,5]
target = 8
sol = Solution()

print(sol.threeSumMulti(arr,target))