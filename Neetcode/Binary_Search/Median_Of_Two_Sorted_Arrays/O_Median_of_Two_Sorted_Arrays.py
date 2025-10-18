from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Apilar elementos por orden de magnitud
        # Sacar la mediana:
            # Si es un numero inpar: Usamos los dos medios
            # Si es par, la mitad es mi respuesta
        
        steps = (len(nums1)) + (len(nums2))
        pointer1 = 0
        pointer2 = 0
        combo = []
        for i in range(0,steps):
            if pointer1 == len(nums1):
                for j in range(pointer2, len(nums2)):
                    combo.append(nums2[j])
                break
            elif pointer2 == len(nums2):
                for j in range(pointer1, len(nums1)):
                    combo.append(nums1[j])
                break


            if nums1[pointer1] <= nums2[pointer2]:
                combo.append(nums1[pointer1])
                pointer1+=1
                print("Hola")
            else:
                combo.append(nums2[pointer2])
                pointer2+=1
                print("Bye")

        # Ahora toca sacar la median al combo

        if len(combo)%2 == 0:
            return (combo[len(combo)//2] + combo[len(combo)//2-1]) / 2
        else:
            return combo[(len(combo)//2)]
        
nums1 = [1,3]
nums2 = [2]

sol = Solution()

print(sol.findMedianSortedArrays(nums1,nums2))

