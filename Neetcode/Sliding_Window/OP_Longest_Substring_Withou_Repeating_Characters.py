from typing import List

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = set()

        l = 0
        res = 0

        for r in range(len(s)):
            while s[r] in chars: # While s[r] is a duplicate
                chars.remove(s[l]) # Remove first char (l)
                l += 1
            chars.add(s[r]) # When there are no duplicates, I can add my char
            res = max(res, r - l + 1)

        return res
    
s="abcabcbb"

sol = Solution()
print(sol.lengthOfLongestSubstring(s))