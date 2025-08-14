from typing import List
from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        Frequency = defaultdict(int)
        output = [None] * k
        for s in nums:
            Frequency[s] += 1

        for i in range(k):
            max_key = max(Frequency, key=Frequency.get)
            output[i] = max_key
            Frequency[max_key] = -1
                   
        return list(output)
    
# Test cases

nums = [1,2,2,3,3,3]
k = 2

sol = Solution()
print(sol.topKFrequent(nums, k))

