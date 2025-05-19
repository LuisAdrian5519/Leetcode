#Convert a list to a set to avoid repetition of elements. 
# If the length of the set is less than the length of the list, then there are duplicates.

from typing import List

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) < len(nums)