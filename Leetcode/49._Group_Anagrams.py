from collections import defaultdict

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        res = defaultdict(list)

        for string in strs:
            count = [0] * 26

            for char in string:
                count[ord(char) - ord("a")] += 1

            res[tuple(count)].append(string)

        return res.values()
    

strs = ["eat","tea","tan","ate","nat","bat"]

sol = Solution()

print(sol.groupAnagrams(strs))